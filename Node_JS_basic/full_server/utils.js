const fs = require('fs');

const readDatabase = (file) => {
  return new Promise((resolve, reject) => {
    fs.readFile(file, 'utf-8', (error, data) => {
      if (error) {
        reject((error));
      } else {
        let message = '';
        const response = [];

        const removeNewLine = data.split('\n');
        removeNewLine.shift();
        const students = removeNewLine.filter((element) => element).map((students) => students.split(','));
        message = `Number of students: ${students.length}`;
        console.log(message);
        response.push(message);
      }
    }
    )
  }
  )
}
export default readDatabase;
