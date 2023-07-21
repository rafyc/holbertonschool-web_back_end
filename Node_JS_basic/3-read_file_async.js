const fs = require('fs');

function countStudents(file) {
  return new Promise((resolve, reject) => {
    fs.readFile(file, 'utf-8', (error, data) => {
      if (error) {
        reject(Error('Cannot load the database'));
      } else {
        let message = '';
        const response = [];

        const removeNewLine = data.split('\n');
        removeNewLine.shift();
        const students = removeNewLine.filter((element) => element).map((students) => students.split(','));
        message = `Number of students: ${students.length}`;
        console.log(message);
        response.push(message);

        const speciality = [];
        students.forEach((student) => {
          const elements = student[3];
          if (!speciality.includes(elements)) {
            speciality.push(elements);
          }
        });

        speciality.forEach((spe) => {
          const studentsBySpe = students.filter((element) => element[3] === spe);
          const namesStudents = [];
          studentsBySpe.forEach((student) => {
            namesStudents.push(student[0]);
          });
          message = `Number of students in ${spe}: ${studentsBySpe.length}. List: ${namesStudents.join(', ')}`;
          console.log(message);
          response.push(message);
        });

        resolve(response);
      }
    });
  });
}

module.exports = countStudents;
// const fs = require('fs/promises');

// const countStudents = async (path) => {
//   try {
//     const data = await fs.readFile(path, { encoding: 'utf8' });

//     const removeHeader = data.split('\n');
//     removeHeader.shift();
//     const cleanArr = removeHeader.filter((e) => e);
//     let num = cleanArr.length;

//     console.log(`Number of students: ${num}`);

//     const all = cleanArr.map((el) => el.split(','));

//     const spe = ['CS', 'SWE'];

//     spe.forEach((el) => {
//       const studentsWithField = all.filter((e) => e[3] === el);
//       const names = studentsWithField.map((e) => e[0]).join(', ');
//       console.log(`Number of students in ${el}: ${studentsWithField.length}. List: ${names}`);
//     });
//   } catch (e) {
//     throw new Error('Cannot load the database');
//   }
// };

// module.exports = countStudents;
