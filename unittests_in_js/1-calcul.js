const calculateNumber = (type, a, b) => {

  const arg1 = Math.round(a);
  const arg2 = Math.round(b);

  switch (type) {
    case 'SUM':
      return arg1 + arg2;
    case 'SUBTRACT':
      return arg1 - arg2;
    case 'DIVIDE':
      return (arg2 === 0) ? 'Error' : arg1 / arg2;
    default:
      throw new Error('The type parameter only accept SUM, SUBTRACT, or DIVIDE');
  }
}

module.exports = calculateNumber;
