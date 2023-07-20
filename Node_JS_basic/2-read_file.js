const fs = require('fs');

const countStudents = (path) => {
  try {
    const data = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' });

    const remove_header = data.split('\n');
    remove_header.shift();
    const clean_arr = remove_header.filter((e) => e);
    for (let i = 0; i <= clean_arr.length; i++)
      num = i;

    console.log(`Number of students: ${num}`);

    const all = clean_arr.map((el) => el.split(','));

    const spe = ['CS', 'SWE'];

    spe.forEach(el => {
      const studentsWithField = all.filter((e) => e[3] === el);
      const names = studentsWithField.map((e) => e[0]).join(', ');
      console.log(`Number of students in ${el}: ${all.filter((e) => e[3] == el).length}. List: ${names}`);
    });

  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
