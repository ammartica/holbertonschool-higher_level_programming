#!/usr/bin/node
// Class Rectangle creates rectangle with instance methods rotate() and double()

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

  // Instance method rotate() exchanges width and height
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Instance method double() multiplies the width and the height by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
