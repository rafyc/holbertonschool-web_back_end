const http = require('node:http');

const app = http.createServer((req, res) => {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});

app.listen(1245);
module.exports = app;
