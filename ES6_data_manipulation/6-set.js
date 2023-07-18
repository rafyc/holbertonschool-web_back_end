export default function setFromArray(Array) {
  const mySet1 = new Set();
  Array.map((x) => mySet1.add(x));
  return mySet1;
}
