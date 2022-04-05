#!/usr/bin/node
// Class Rectangle creates empty rectangle if w or h are <= 0

class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
