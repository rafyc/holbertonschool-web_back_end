const getListStudents = () => {

  let students = []

  let student = {}
  student.firstName = "Guillaume"
  student.id = 1
  student.location = "San Francisco"
  students.push(student)

  let student1 = {}
  student1.firstName = "James"
  student1.id = 2
  student1.location = "Columbia"
  students.push(student1)

  let student2 = {}
  student2.firstName = "Serena"
  student2.id = 2
  student2.location = "San Francisco"
  students.push(student2)

  return students

}

export default getListStudents
