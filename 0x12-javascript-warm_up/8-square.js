#!/usr/bin/node
// Prints a square the size of x

const x = process.argv[2];

if (parseInt(x)) {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
} else {
  console.log('Missing size');
}
