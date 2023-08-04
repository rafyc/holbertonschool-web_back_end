const { log } = require('console');
const express = require('express');
const redis = require('redis');
const util = require('util')

// Utils
const itemError = { "status": "Product not found" }
const noItemInStock = { "status": "Not enough stock available", "itemId": 1 }
const itemReserved = { "status": "Reservation confirmed", "itemId": 1 }

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 3 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 10', price: 550, stock: 5 },
];
const getItemById = (id) => listProducts.find((el) => el.id === id);

// Redis
const client = redis.createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log(`Redis client connected to the server`));

const reserveStockById = (id, stock) => {
  client.set(id, stock, redis.print)
};

const getCurrentReservedStockById = async (itemId) => {
  try {
    const getAsync = util.promisify(client.get).bind(client);
    const value = await getAsync(itemId);
    return value;
  }
  catch (err) {
    console.log(err);
    throw err;
  }
}

// API Express
const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.send(JSON.stringify(listProducts))
})

app.get('/list_products/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId)
  const item = getItemById(itemId)
  !item && res.send(itemError);
  res.send(item)
})

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId)
  const item = getItemById(itemId)
  const status = { "status": "Reservation confirmed", "itemId": `${itemId}` }
  const currentStock = await getCurrentReservedStockById(itemId)

  !item && res.send(itemError);
  if (parseInt(currentStock) < 1) {
    res.send(noItemInStock)
  }
  else {
    reserveStockById(itemId, (parseInt(currentStock) - 1))
    console.log(parseInt(currentStock));
    res.send(status)
  }
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
  listProducts.forEach((product) => {
    reserveStockById(product.id, product.stock);
  })
})


module.exports = app;
