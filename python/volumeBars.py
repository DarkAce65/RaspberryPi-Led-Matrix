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
barWidth = width / 4
pi = numpy.pi
barHeights = numpy.array([0, pi / 4, pi / 2, pi * 3 / 4])

while True:
	nextFrame = ledMatrix.CreateFrameCanvas()
	heights = numpy.sin(barHeights)
	barHeights += pi / 4
	for x in range(width):
		barHeight = int(heights[int(x / barWidth)] * height)
		for y in range(height):	
			if height - y <= barHeight:
				nextFrame.SetPixel(x, y, randint(0, 255), randint(0, 255), randint(0, 255))
	ledMatrix.SwapOnVSync(nextFrame)
	time.sleep(0.2)
