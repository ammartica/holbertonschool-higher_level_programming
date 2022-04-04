#!/usr/bin/node
// Prints the addition of 2 integers

// Computes factorial using recursion
function factorial (x) {
  if (!x) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
