export default function hasValuesFromArray(set, array) {
  if (array.map(x => set.has(x)).every(Boolean))
    return true;
  return false;
};
