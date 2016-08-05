#include "led-matrix.h"

#include <iostream>
#include <unistd.h>
#include <math.h>
#include <stdio.h>

using rgb_matrix::GPIO;
using rgb_matrix::RGBMatrix;
using rgb_matrix::Canvas;

class Ball {
	int r, g, b;
	float x, y, vx, vy;
public:
	static const int GRAVITY = -20;
	Ball(float x, float y, float vx, float vy, int r, int g, int b): x(x), y(y), vx(vx), vy(vy), r(r), g(g), b(b) {}
	void updateValues(float timeElapsed) {
		x += vx * timeElapsed;
		y += vy * timeElapsed + 0.5 * Ball::GRAVITY * pow(timeElapsed, 2);
		vy += Ball::GRAVITY * timeElapsed;
		edgeHandling(timeElapsed);
	}
	void edgeHandling(float timeElapsed) {
		if((int) y == 0) {
			vx -= copysign(1, vx) * timeElapsed;
		}

		if(x < 0) {
			vx = abs(vx);
			x = 0;
		}
		else if(x > 31) {
			vx = abs(vx) * -1;
			x = 31;
		}

		if(y < 0) {
			vy = abs(vy) * 0.95; // Bounce decay
			y = 0;
		}
		else if(y > 15) {
			vy = abs(vy) * -0.95; // Bounce decay
			y = 15;
		}
	}
	void drawOnCanvas(Canvas *canvas) {
		canvas->SetPixel((int) x, canvas->height() - 1 - (int) y, r, g, b);
	}
	void printValues() {
		std::cout << "x: " << x << " y: " << y << " vx: " << vx << " vy: " << vy << std::endl;
	}
};

static void DrawOnCanvas(Canvas *canvas) {
	Ball *red = new Ball(2, 12, 4, -4, 255, 0, 0);
	Ball *blue = new Ball(6, 9, 15, 12, 0, 0, 255);
	int c = 0;
	while(c < 60000) {
		red->updateValues(1 / 60.0);
		blue->updateValues(1 / 60.0);
		red->drawOnCanvas(canvas);
		blue->drawOnCanvas(canvas);
		c++;
		usleep(1000000 / 60.0);
		canvas->Clear();
	}
}

int main(int argc, char *argv[]) {
	GPIO io;
	if(!io.Init()) {
		return 1;
	}

	Canvas *canvas = new RGBMatrix(&io, 16, 1, 1);
	DrawOnCanvas(canvas);

	canvas->Clear();
	delete canvas;

	return 0;
}
