export default class HolbertonCourse {
  constructor(name, length, students) {

    this.name = name;

    this.length = length;

    this.students = students;
  }

  // SETTERS

  set name(inputName) {
    if (typeof inputNameame !== "string")
      throw new TypeError('Name must be a string')
    this._name = inputName;
  }

  set length(inputLength) {
    if (typeof inputLength !== "number")
      throw new TypeError('Length must be a number')
    this._length = inputLength;
  }
  set student(inputStudent) {
    if (!Array.isArray(inputStudent) && !inputStudent.every((s) => typeof s === 'string'))
      throw new TypeError('Students must be an array of strings');
    this._student = inputStudent;
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
