#!/usr/bin/node
// Searches second biggest integer in list of arguments

const len = process.argv.length;
const argList = process.argv.slice(2);

if (len < 3) {
  console.log('0');
} else if (len === 3) {
  console.log('1');
} else {
  argList.sort().reverse();
  const secondLargest = argList[1];
  console.log(secondLargest);
}
