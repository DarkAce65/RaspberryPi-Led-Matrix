#!/usr/bin/env python
from rgbmatrix import RGBMatrix
from random import randint
import numpy
import math
import time

rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)

height = ledMatrix.height
width = ledMatrix.width
barWidth = width / 16
pi = numpy.pi
barHeights = numpy.array([])
for i in range(16):
	barHeights[i] = i * pi / 16

while True:
	nextFrame = ledMatrix.CreateFrameCanvas()
	heights = numpy.sin(barHeights)
	barHeights += pi / 16
	for x in range(width):
		barHeight = int(heights[int(x / barWidth)] * height)
		for y in range(height):
			if height - y <= barHeight:
				if y < 2:
					nextFrame.SetPixel(x, y, 255, 0, 0)
				elif y < 6:
					nextFrame.SetPixel(x, y, 200, 200, 0)
				else:
					nextFrame.SetPixel(x, y, 0, 200, 0)
	ledMatrix.SwapOnVSync(nextFrame)
	time.sleep(0.2)
