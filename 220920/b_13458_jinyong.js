var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString();
let N = input();
let students = input.split(" ");
let BC = input().split(" ");
let B = Number(BC[0])
let C = Number(BC[1])

// let students = ["3", "4", "5"];
// let B = Number("2")
// let C = Number("2")

let answer = 0;

students.map((student_str) => {
  let student = Number(student_str)

  answer += 1

  if (student > B) {
    student -= B
    answer += parseInt(student / C)
  
    if (student % C) {
      answer += 1
    }
  }
})

console.log(answer)
