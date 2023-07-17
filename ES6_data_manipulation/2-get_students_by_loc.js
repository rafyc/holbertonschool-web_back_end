const getStudentsByLocation = (students, city) => {
  return students.filter((item) => item.location === city);
}
