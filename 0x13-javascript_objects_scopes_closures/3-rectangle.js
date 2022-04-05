#!/usr/bin/node
// Class Rectangle creates rectangle and has instance method print()

class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Instance method print() prints a rectangle using character X
  print (chara = 'X') {
    let stringRect = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        stringRect += chara;
      }
      if (i !== this.height - 1) {
        stringRect += '\n';
      }
    }
    console.log(stringRect);
  }
}
module.exports = Rectangle;
