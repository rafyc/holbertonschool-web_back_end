export default function appendToEachArrayValue(array, appendString) {
  let newArray = []
  for (let element of array) {
    newArray.push(appendString + element);
  }

  return newArray;
}
