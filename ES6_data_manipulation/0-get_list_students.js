const getListStudents = () => {

  const students = []

  const student = {}
  student.id = 1
  student.firstName = "Guillaume"
  student.location = "San Francisco"
  students.push(student)

  const student1 = {}
  student1.id = 2
  student1.firstName = "James"
  student1.location = "Columbia"
  students.push(student1)

  const student2 = {}
  student2.id = 2
  student2.firstName = "Serena"
  student2.location = "San Francisco"
  students.push(student2)

  return students;

}

export default getListStudents;
