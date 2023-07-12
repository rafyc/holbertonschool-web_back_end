export default function createIteratorObject(report) {
  const arr = [];
  for (let name of Object.values(report.allEmployees))
    arr.push(...name);
  return arr
};
