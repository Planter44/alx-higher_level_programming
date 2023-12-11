#!/usr/bin/node

class Rectangle {
  constructor (a, b) {
    if (b > 0 && a > 0) {
      this.width = a;
      this.height = b;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
