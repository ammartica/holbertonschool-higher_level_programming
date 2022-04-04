#!/usr/bin/node
// Prints "C is fun" x times

const x = process.argv[2];

if (parseInt(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
