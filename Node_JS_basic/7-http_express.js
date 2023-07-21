const express = require('express');
const process = require('process');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const db = process.argv[2];


app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(db)
    .then((data) => {
      res.send(`This is the list of our students \n${data.join('\n')}`);
    })
    .catch((err) => {
      res.send(`${err.message}`);
    });
});

app.listen(port);
module.exports = app;
