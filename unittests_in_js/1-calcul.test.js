var assert = require('assert');
const calculateNumber = require("./1-calcul.js");
describe('SUM', function () {
  it('should round and add', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  })
});
describe('SUBTRACT', function () {
  it('should round and subtract', function () {
    assert.strictEqual(calculateNumber(1, 3), -2);
  })
});
describe('DIVIDE', function () {
  it('should round and divid', function () {
    assert.strictEqual(calculateNumber(1, 3), 0.3333333333333333);
  })
});


