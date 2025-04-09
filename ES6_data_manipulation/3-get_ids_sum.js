// Create a function getStudentIdsSum that returns the sum of all the student ids.

// It should accept a list of students (from getListStudents) as a parameter.

// You must use the reduce function on the array.

// bob@dylan:~$ cat 3-main.js
// import getListStudents from "./0-get_list_students.js";
// import getStudentIdsSum from "./3-get_ids_sum.js";

// const students = getListStudents();
// const value = getStudentIdsSum(students);

// console.log(value);

// bob@dylan:~$
// bob@dylan:~$ npm run dev 3-main.js
// 8
// bob@dylan:~$

export default function getStudentIdsSum(students) {
  return students.reduce((sum, student) => sum + student.id, 0);
}
