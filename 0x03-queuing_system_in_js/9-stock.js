import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const app = express();
const port = 1245;
const clientGet = promisify(client.get).bind(client);

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

const getItemById = (id) => {
  return listProducts.find((item) => item.itemId === id);
};

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock, (err, reply) => reply);
};

const getCurrentReservedStockById = async (itemId) => {
  const stock = await clientGet(`item.${itemId}`);
  return stock;
};

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  if (stock === 'undefined') {
    res.status(404).json({ status: 'Product not found' });
    return;
  }

  const stock =
    currentStock !== null ? currentStock : item.initialAvailableQuantity;

  item.currentQuantity = stock;
  res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }

  let currentStock = await getCurrentReservedStockById(itemId);

  if (currentStock === null) {
    currentStock = item.initialAvailableQuantity;
  }
  if (currentStock <= 0) {
    res.status(403).json({ status: 'Not enough stock available' });
    return;
  }

  reserveStockById(itemId, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId: itemId });
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
