#!/usr/bin/node
// Child Class Square with instance method charPrint(c)

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let str = '';

    for (let index = 0; index < this.height; index++) {
      str += c;
    }

    for (let index = 0; index < this.height; index++) {
      console.log(str);
    }
  }
};
