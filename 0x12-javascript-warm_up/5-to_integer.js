#!/usr/bin/node
// Converts and prints first argument to an integer

const arg = process.argv[2];

if (parseInt(arg)) {
  if (parseInt(arg) % 1 !== 0) {
    console.log('My number:', Math.floor(parseInt(arg)));
  } else {
    console.log('My number:', (parseInt(arg)));
  }
} else {
  console.log('Not a number');
}
