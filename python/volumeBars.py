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
barHeights = numpy.empty([16])
for i in range(16):
	barHeights[i] = i * pi / 16

while True:
	nextFrame = ledMatrix.CreateFrameCanvas()
	heights = numpy.empty([16])
	for i in range(len(barHeights)):
		x = barHeights[i]
		heights[i] = (math.sin(randint(-3, 3) * x) + math.cos(randint(-3, 3) * x) + math.cos(randint(-3, 3) * x)) / 3

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
	time.sleep(0.1)
