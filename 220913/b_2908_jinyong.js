var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString();
let input_value = input.split(" ");

let num_1 = input_value[0];
let num_2 = input_value[1];

let reverse_num_1 = Number(String(num_1).split("").reverse().join(""))
let reverse_num_2 = Number(String(num_2).split("").reverse().join(""))

if (reverse_num_1 > reverse_num_2) {
  console.log(reverse_num_1);
} else {
  console.log(reverse_num_2);
};
