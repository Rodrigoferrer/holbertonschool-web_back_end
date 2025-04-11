function updateStudentGradeByCity(students, city, newGrades) {
  const filteredStudents = students.filter((i) => i.location === city);

  const updatedStudents = filteredStudents.map((i) => {
    const gradeObj = newGrades.find((grade) => grade.studentId === i.id);
    return {
      id: i.id,
      firstName: i.firstName,
      location: i.location,
      grade: gradeObj ? gradeObj.grade : 'N/A',
    };
  });

  return updatedStudents;
}
export default updateStudentGradeByCity;
