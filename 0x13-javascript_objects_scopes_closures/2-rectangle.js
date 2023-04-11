#!/usr/bin/node
//JS script to create a class
class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
}
module.exports = Rectangle;
