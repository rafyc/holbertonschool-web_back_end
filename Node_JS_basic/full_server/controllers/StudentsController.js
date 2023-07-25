import readDatabase from "../utils";

class StudentsController {
  static getAllStudents(request, response, file) {
    readDatabase(file)
      .then((data) => {
        console.log(data);
        response.status(200).send(data); // Send the data in the response
      })
      .catch((err) => {
        console.error(err);
        response.status(500).send("Cannot load the database"); // Send an error response
      });
  }

  static getAllStudentsByMajor(request, response, file) {
    readDatabase(file)
      .then((data) => {
        console.log(data);
        response.status(200).send(data); // Send the data in the response
      })
      .catch((err) => {
        console.error(err);
        response.status(500).send("Cannot load the database"); // Send an error response
      });
  }
}

export default StudentsController;
