const fs = require('fs');

const countStudents = (path) => {
  try {
    const data = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' });

    const removeHeader = data.split('\n');
    removeHeader.shift();
    const cleanArr = removeHeader.filter((e) => e);
    for (let i = 0; i <= cleanArr.length; i += 1) {
      num = i;
    }

    console.log(`Number of students: ${num}`);

    const all = cleanArr.map((el) => el.split(','));

    const spe = ['CS', 'SWE'];

    spe.forEach((el) => {
      const studentsWithField = all.filter((e) => e[3] === el);
      const names = studentsWithField.map((e) => e[0]).join(', ');
      console.log(`Number of students in ${el}: ${all.filter((e) => e[3] === el).length}. List: ${names}`);
    });
  } catch (e) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
