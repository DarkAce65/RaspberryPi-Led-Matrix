#include "led-matrix.h"

#include <unistd.h>
#include <math.h>
#include <stdio.h>
#include <signal.h>

using rgb_matrix::GPIO;
using rgb_matrix::RGBMatrix;
using rgb_matrix::Canvas;

volatile bool interrupt_received = false;
static void interrupt_handler(int signo) {
	interrupt_received = true;
}

static void draw_on_canvas(Canvas *canvas) {
	canvas->Fill(0, 0, 20);

	int center_x = canvas->width() / 2;
	int center_y = canvas->height() / 2;
	canvas->SetPixel(center_x, center_y, 255, 0, 0);
	usleep(1000 * 1000);
}

int main(int argc, char *argv[]) {
	RGBMatrix::Options defaults;
	defaults.hardware_mapping = "regular";
	defaults.rows = 16;
	defaults.chain_length = 1;
	defaults.parallel = 1;
	defaults.show_refresh_rate = true;

	Canvas *canvas = rgb_matrix::CreateMatrixFromFlags(&argc, &argv, &defaults);
	if(canvas == NULL) {
		return 1;
	}

	signal(SIGTERM, interrupt_handler);
	signal(SIGINT, interrupt_handler);

	draw_on_canvas(canvas);

	canvas->Clear();
	delete canvas;

	return 0;
}
