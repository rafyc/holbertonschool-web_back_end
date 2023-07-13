export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  try {
    return (numerator / denominator);
  } catch (e) {
    console.log(e);
  }
  return undefined
}
