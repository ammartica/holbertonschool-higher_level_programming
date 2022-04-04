#!/usr/bin/node
// Converts and prints first argument to an integer

const arg = process.argv[2];
const convertedArg = parseInt(arg);

if (parseInt(arg)) {
  if (convertedArg % 1 !== 0) {
    console.log('My number:', Math.floor(covertedArg));
  } else {
    console.log('My number:', (convertedArg));
  }
} else {
  console.log('Not a number');
}
