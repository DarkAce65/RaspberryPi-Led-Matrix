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
		r = y % 8 / 7 * 255
		g = x % 8 / 7 * 255
		b = (x % 8 + y % 8) / 14 * 255
		ledMatrix.SetPixel(x, y, r, g, b)
		time.sleep(0.05)

time.sleep(5)
ledMatrix.Clear()