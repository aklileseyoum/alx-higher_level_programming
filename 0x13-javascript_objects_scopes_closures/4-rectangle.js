#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(('X'.repeat(this.width) + '\n').repeat(this.height - 1) + 'X'.repeat(this.width));
  }
	rotate () {
		let temp = this.width;
		this.width = this.height;
		this.height = temp;
	}

	double () {
		this.width = this.width * 2;
		this height = this.height * 2;
	}
}
module.exports = Rectangle;
