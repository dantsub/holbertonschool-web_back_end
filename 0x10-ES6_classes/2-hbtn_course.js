export default class HolbertonCourse {
  constructor(name, length, students) {

    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    if (!Array.isArray(students)) throw TypeError('Stundents must be an array of Strings');
    if (students.every((student) => typeof student !== 'string')) throw TypeError('Stundents must be an array of Strings');

    this._name = name;
    this._length = length;
    this._students = students;
  }
  /* getter name */
  get name() {
    return this._name;
  }
  /* setter name */
  set name(value) {
    this._name = value;
  }
  /* getter length */
  get length() {
    return this._length;
  }
  /* setter length */
  set length(value) {
    this._length = value;
  }
  /* getter students */
  get students() {
    return this._students;
  }
  /* setter students */
  set students(value) {
    this._students = value;
  }
}
