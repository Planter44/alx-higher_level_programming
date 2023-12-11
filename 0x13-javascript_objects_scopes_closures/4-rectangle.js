#!/usr/bin/node
module.exports = class Rectangle {
  constructor (a, b) {
    if (typeof a === 'number' && typeof b === 'number' && a > 0 && b > 0) {
      this.a = a;
      this.b = b;
    }
  }

  print (char = 'X') {
    for (let i = 0; i < this.b; ++i) {
      let j = 0;

      for (; j < this.a; ++j) {
        process.stdout.write(char);
      }

      if (j === this.a) {
        console.log('');
      }
    }
  }
  rotate () {
    [this.a, this.b] = [this.b, this.a];
  }

  double () {
    this.a *= 2;
    this.b *= 2;
  }
};
