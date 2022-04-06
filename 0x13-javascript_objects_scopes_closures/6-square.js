#!/usr/bin/node
// Child Class Square with instance method charPrint(c)

const fSquare = require('./5-square.js');

class Square extends fSquare {
  constructor (size) {
    super(size, size);
  }

  // Instance method prints rectangle using the character c
  charPrint (c) {
    super.print(c);
  }
}

module.exports = Square;
