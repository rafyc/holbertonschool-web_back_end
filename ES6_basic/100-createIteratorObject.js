export default function createIteratorObject(report) {
  const arr = [];
  for (const name of Object.values(report.allEmployees)) {
    arr.push(...name);
  }
  return arr;
}
