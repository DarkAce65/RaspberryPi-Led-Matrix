#!/usr/bin/env python
from rgbmatrix import RGBMatrix
from random import randint
import sys, time

rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)
height = ledMatrix.height
width = ledMatrix.width

try:
	print "Press Ctrl + C to stop executing"
	for x in range(width):
		for y in range(height):
			r = int(y % 8 / 7.0 * 255)
			g = int(x % 8 / 7.0 * 255)
			b = int((int(x / 8) + int(y / 8) * 4) / 7.0 * 255)
			ledMatrix.SetPixel(x, y, r, g, b)
			time.sleep(0.02)

	time.sleep(5)
	ledMatrix.Clear()
except KeyboardInterrupt:
	print "Exiting\n"
	sys.exit(0)