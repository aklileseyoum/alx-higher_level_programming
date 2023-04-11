#!/usr/bin/node
//JS script to draw a box
class Rectangle {
        constructor(w, h) {
                if (w > 0 && h > 0) {
                        this.width == w;
                        this.height == h;
                }
        }

        print () {
                for (let i = 0; i < height; i++) {
                        for (let j = 0; j < width; j++) {
                                console.log('X');
                        }
                        console.log('\n');
                }
        }

	rotate () {
		let temp = width;
		width = height:
		height = temp;
	}

	double () {
		width = width * 2;
		height = height * 2;
	}
}
module.exports = Rectangle;
