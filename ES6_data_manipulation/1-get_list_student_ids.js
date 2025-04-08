// Create a function getListStudentIds that returns an array of ids from a list of object.

// This function is taking one argument which is an array of objects -
//  and this array is the same format as getListStudents from the previous task.

// If the argument is not an array, the function is returning an empty array.

// You must use the map function on the array.

// bob@dylan:~$ cat 1-main.js
// import getListStudentIds from "./1-get_list_student_ids.js";
// import getListStudents from "./0-get_list_students.js";

// console.log(getListStudentIds("hello"));
// console.log(getListStudentIds(getListStudents()));

// bob@dylan:~$
// bob@dylan:~$ npm run dev 1-main.js
// []
// [ 1, 2, 5 ]
// bob@dylan:~$
import { getListStudents } from './0-get_list_students';

export default function getListStudentsIds() {
  if (!Array.isArray(students)) {
    return [];
  }
  const studentsId = students.map((student) => student.id);
  return studentsId;
}
