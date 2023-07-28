const Utils = require('./utils');

const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
  const utils = Utils();
  const sum = utils.calculateNumber('SUM', totalAmount, totalShipping)
  console.log(`The total is: ${sum}`);
  return sum;
}

module.exports = sendPaymentRequestToApi;
