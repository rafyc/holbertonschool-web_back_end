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
        response.status(500).send("Cannot load the database"); // Send an error response
      });
  }

  static getAllStudentsByMajor(request, response, file) {
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
}

export default StudentsController;
