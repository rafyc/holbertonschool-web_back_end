export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(inputName) {
    if (typeof inputName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = inputName;
  }

  set length(inputLength) {
    if (typeof inputLength !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = inputLength;
  }

  set students(inputStudents) {
    if (!Array.isArray(inputStudents) && !inputStudents.every((s) => typeof s === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = inputStudents;
  }
}
