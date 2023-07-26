const calculateNumber = (type, a, b) => {
  if (type.includes('SUM')) {
    return Math.round(a) + Math.round(b);
  } else if (type.includes('SUBTRACT')) {
    return Math.round(a) - Math.round(b);
  } else if (type.includes('DIVIDE')) {
    if (b === 0) {
      return ('Error')
    }
    return Math.round(a) / Math.round(b);
  } else {
    return 'Error';
  }
};

module.exports = calculateNumber;
