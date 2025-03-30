// Implement a class named Car:

// Constructor attributes:
// brand (String)
// motor (String)
// color (String)
// Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
// Add a method named cloneCar. This method should return a new object of the class.

export default class Car {
  constructor(brand, motor, color) {
    if (typeof brand !== 'string') throw new TypeError('Subject must be a string');
    if (typeof motor !== 'string') throw new TypeError('Subject must be a string');
    if (typeof color !== 'string') throw new TypeError('Subject must be a string');

    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const newObject = new this.constructor(this._brand, this._motor, this._color);
    return newObject;
  }
}
