function printStudents(students) {
    // Print each student name from an array
    console.log("Student List:");
    for (let student of students) {
        console.log(student);
    }
}

// Test with sample student names
const studentNames = ["Alice", "Bob", "Charlie"];
printStudents(studentNames);
