const redis = require('redis');
const client = redis.createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log(`Redis client connected to the server`));

const hbtnChannel = 'holberton school channel'

client.subscribe(hbtnChannel)
client.on('message', (channel, message) => {
  if (channel === hbtnChannel) {
    console.log(message);
  }
  if (message === 'KILL_SERVER') {
    client.quit();
  }
})
