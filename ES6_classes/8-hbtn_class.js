// Implement a class named HolbertonClass:

// Constructor attributes:
// size (Number)
// location (String)
// Each attribute must be stored in an “underscore” attribute version
// (ex: name is stored in _name)
// When the class is cast into a Number, it should return the size.
// When the class is cast into a String, it should return the location.
// salida

export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') throw new TypeError('Size must be a number');
    if (typeof location !== 'string') throw new TypeError('location must be a string');
    this._size = size;
    this._location = location;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
