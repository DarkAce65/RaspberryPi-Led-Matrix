#!/usr/bin/env python
from rgbmatrix import RGBMatrix
from random import randint
import time

rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)
height = ledMatrix.height
width = ledMatrix.width

for x in range(width):
	for y in range(height):
		r = int(y % 8 / 7 * 255)
		g = int(x % 8 / 7 * 255)
		b = int((int(x / 8) + int(y / 8) * 4) / 7 * 255)
		ledMatrix.SetPixel(x, y, r, g, b)
		time.sleep(0.05)

time.sleep(5)
ledMatrix.Clear()