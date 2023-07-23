export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building
      && typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set(newSqtf) {
    if (typeof newSqtf !== 'number') {
      throw new Error('sqft must be a number')
    }
    this._sqft = newSqtf
  }

  evacuationWarningMessage() {

  }
}
