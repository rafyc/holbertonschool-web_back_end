export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== "string")
      console.error('Name must be a string')
    this.name = name;
    if (typeof length !== "number")
      console.error('Length must be a number')
    this.length = length;
    if (!Array.isArray(students) && !students.every((s) => typeof s === 'string'))
      console.error('Students must be an array of strings');
    this.students = students;
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
