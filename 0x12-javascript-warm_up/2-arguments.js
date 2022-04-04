#!/usr/bin/node
// Prints message depnding on number of arguments passed

const len = process.argv.length;

if (len > 3) {
  console.log('Arguments found');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
