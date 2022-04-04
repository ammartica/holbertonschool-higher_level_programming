#!/usr/bin/node
// Prints first argument passed to it

const len = process.argv.length;
const arg = process.argv[2];

if (len === 3) {
  console.log(arg);
} else {
  console.log('No argument');
}
