import redis from 'redis';

const client = redis.createClient();

const obj = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
};

Object.entries(obj).forEach(([key, value]) => {
  client.hset('HolbertonSchools', key, value, redis.print);
});

client.hgetall('HolbertonSchools', (err, reply) => {
  console.log(reply);
});
