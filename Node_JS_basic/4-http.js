const http = require('node:http');

// Create a local server to receive data from
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end('Hello Holberton School!');
});

app.listen(1245);
