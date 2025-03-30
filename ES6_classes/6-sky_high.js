// Import Building from 5-building.js.

// Implement a class named SkyHighBuilding that extends from Building:

// Constructor attributes:
// sqft (Number) (must be assigned to the parent class Building)
// floors (Number)
// Each attribute must be stored in an “underscore” attribute version
// (ex: name is stored in _name)
// Implement a getter for each attribute.
// Override the method named evacuationWarningMessage and return the
// following string Evacuate slowly the NUMBER_OF_FLOORS floors

/* eslint-disable import/extensions */
import Building from './5-building.js';

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}

export default SkyHighBuilding;
