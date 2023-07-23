export default class Building {
  constructor(sqft) {
    this.sqft = sqft;
  }

  get() {
    return this._sqft;
  }

  set(newSqtf) {
    if (typeof newSqtf !== 'number') {
      throw new Error('sqft must be a number')
    }
    this._sqft = newSqtf
  }
}
