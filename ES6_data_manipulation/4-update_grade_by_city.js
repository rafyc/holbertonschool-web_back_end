const updateStudentGradeByCity = (students, city, newGrades) => {
  if (!newGrades.grade) {
    newGrades.grade = 'N/A'
  }
  const filteredStudent = students.filter(item => item.location === city);
  return filteredStudent.map(item => item.grade = newGrades)
};

export default updateStudentGradeByCity;
