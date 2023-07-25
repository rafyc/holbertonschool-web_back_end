import readDatabase from '../utils';
class StudentsController {
  static getAllStudents(request, response, file) {
    readDatabase(file)
      .then((data) => {
        const formattedData = data.join('\n'); // Join the elements with newline characters
        console.log(formattedData);
        response.status(200).send(`This is the list of our students\n${formattedData}`); // Send the formatted data in the response
      })
      .catch((err) => {
        console.error(err);
        response.status(500).send('Cannot load the database'); // Send an error response
      });
  }


  static getAllStudentsByMajor(request, response, file) {

    readDatabase(file)

      .then((data) => {
        if (request.path.includes('SWE')) {
          data = data[0]
        } else if (request.path.includes('CS')) {
          data = data[1]
        }
        else {
          response.status(500).send('Major parameter must be CS or SWE');
        }

        const afterColon = data.split('List: ')[1].trim();
        response.status(200).send(`${afterColon}`); // Send the formatted data in the response
      })
      .catch((err) => {
        console.error(err);
        response.status(500).send('Cannot load the database'); // Send an error response
      });
  }
}

export default StudentsController;
