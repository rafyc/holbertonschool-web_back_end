import { createClient } from 'redis';
import redis from 'redis'
import { promisify } from 'util';

const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log(`Redis client connected to the server`));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print)
}
const displaySchoolValue = async (schoolName) => {
  try {
    const getAsync = promisify(client.get).bind(client);
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.log(err);
  }

}




displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
