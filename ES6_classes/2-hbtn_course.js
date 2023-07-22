export default class HolbertonCourse {
  constructor(name, length, student) {
    if (typeof name !== String)
      console.error('Name must be a string')
    this.name = name;
    if (typeof length !== Number)
      console.error('Length must be a number')
    this.length = length;
    if (typeof student !== Array[String])
      console.error('Student must be an array of strings');
    this.student = student;
  }

  // SETTERS

  set name(inputName) {
    return this._name = inputName;
  }

  set length(inputLength) {
    return this._length = inputLength;
  }
  set student(inputStudent) {
    return this._student = inputStudent;
  }

  // GETTERS
  get name() {
    return this._name
  }

  get length() {
    return this._length
  }

  get student() {
    return this._student
  }

}
