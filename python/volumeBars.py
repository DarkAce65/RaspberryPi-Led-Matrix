#!/usr/bin/env python
from rgbmatrix import RGBMatrix
from random import randint
import math
import time

rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)

height = ledMatrix.height
width = ledMatrix.width
barWidth = width / 4
barHeights = [0, 45, 90, 135]

while True:
	nextFrame = ledMatrix.CreateFrameCanvas()
	heights = numpy.sin(barHeights * numpy.pi / 180)
	numpy.add(45, barHeights)
	for x in range(width):
		for y in range(height):
			height = int(heights[int(x / barWidth)] * height)
			if y < height
				nextFrame.SetPixel(x, y, randint(0, 255), randint(0, 255), randint(0, 255))
	ledMatrix.SwapOnVSync(nextFrame)
	time.sleep(1)