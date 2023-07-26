var assert = require('assert');
const calculateNumber = require("./0-calcul.js");
describe('calculateNumber', function () {
  it('should round and add', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1.6, 1.8), 4)
    assert.strictEqual(calculateNumber(1, 3.9), 5);
    assert.strictEqual(isNaN(calculateNumber(1,)), true)
  });
});
