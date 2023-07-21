const http = require('http');
const countStudents = require('./3-read_file_async');
const process = require('process');

const hostname = '127.0.0.1';
const port = 1245;
const db = process.argv[2]

const app = http.createServer((request, response) => {
  response.statusCode = 200;
  const { url } = request
  response.setHeader('Content-Type', 'text/plain');


  if (url === '/students') {
    response.write('This is the list of our students\n');
    countStudents(db)
      .then((data) => {
        response.end(`${data.join('\n')}`);
      })
  }
  if (url === '/')
    response.end('Hello Holberton School!');
});

app.listen(port, hostname);
module.exports = app;
