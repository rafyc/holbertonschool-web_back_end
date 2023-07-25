const fs = require('fs');

function readDatabase(file) {
  return new Promise((resolve, reject) => {
    fs.readFile(file, 'utf-8', (error, data) => {
      if (error) {
        reject(Error('Cannot load the database'));
      } else {
        const response = [];
        const removeNewLine = data.split('\n');
        removeNewLine.shift();
        const students = removeNewLine.filter((element) => element).map((students) => students.split(','));

        const speciality = [];
        students.forEach((student) => {
          const elements = student[3];
          if (!speciality.includes(elements)) {
            speciality.push(elements);
          }
        });

        speciality.forEach((spe) => {
          const studentsBySpe = students.filter((element) => element[3] === spe);
          const namesStudents = studentsBySpe.map((student) => student[0]);
          const message = `Number of students in ${spe}: ${studentsBySpe.length}. List: ${namesStudents.join(', ')}`;
          response.push(message);
        });

        resolve(response);
      }
    });
  });
};

module.exports = readDatabase;
