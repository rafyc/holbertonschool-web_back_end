const calculateNumber = (a, b, type) => {
  return (
    type.includes('SUM') && Math.round(a) + Math.round(b) ||
    type.includes('SUBTRACT') && Math.round(a) - Math.round(b) ||
    type.includes('DIVIDE') && b !== 0 && Math.round(a) / Math.round(b) ||
    "Error"
  );
};

module.exports = calculateNumber;
