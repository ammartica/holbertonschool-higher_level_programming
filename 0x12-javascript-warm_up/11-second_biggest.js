#!/usr/bin/node
// Searches second biggest integer in list of arguments

const len = process.argv.length;
const argList = process.argv.slice(2);

if (len <= 3) {
  console.log(0);
} else {
  argList.sort().reverse();
  const secondBig = argList[1];
  console.log(secondBig);
}
