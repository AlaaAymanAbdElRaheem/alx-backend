import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const channel = 'holberton school channel';

client.subscribe(channel);

client.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    console.log(message);
  }
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
});
