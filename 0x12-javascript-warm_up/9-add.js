#!/usr/bin/node
// Prints the addition of 2 integers

// Returns sum of two integers
function add (a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
const sum = add(arg1, arg2);

console.log(sum);
