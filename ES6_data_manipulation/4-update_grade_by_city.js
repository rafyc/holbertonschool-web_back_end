const updateStudentGradeByCity = (students, city, newGrades) => {
  return students
    .filter((item) => item.location === city)
    .map((item) => {
      const obj = newGrades.find(grade => grade.studentId === item.id)
      return { ...item, grade: obj ? obj.grade : 'N/A' };
    });
};

export default updateStudentGradeByCity;
