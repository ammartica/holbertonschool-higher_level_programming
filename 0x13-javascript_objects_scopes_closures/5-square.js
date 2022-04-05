#!/usr/bin/node
// Child Class Square inherits from Parent Class Rectangle

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
