#!/usr/bin/node
// Child Class Square with instance method charPrint(c)

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    super.print(c);
  }
};
