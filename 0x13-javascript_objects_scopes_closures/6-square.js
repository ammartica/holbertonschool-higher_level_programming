#!/usr/bin/node
// Child Class Square with instance method charPrint(c)

const fSquare = require('./5-square');

class Square extends fSquare {
  // Instance method prints rectangle using the character c
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    super.print(c);
  }
}

module.exports = Square;
