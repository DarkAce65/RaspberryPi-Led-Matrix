#!/usr/bin/env python
from rgbmatrix import RGBMatrix
from random import randint
import numpy
import math
import time

pi = numpy.pi
rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)

height = ledMatrix.height
width = ledMatrix.width

numRows = 16
barWidth = width / numRows
tempXAxis = numpy.empty([numRows])
for i in range(numRows):
	tempXAxis[i] = i * pi / numRows

def drawFrame(barHeights): # Takes an array of heights with a range of 0 to 1
	nextFrame = ledMatrix.CreateFrameCanvas()

	for x in range(width):
		barHeight = int(heights[int(x / barWidth)] * height)
		for y in range(height):
			if height - y <= barHeight:
				if y < 2:
					nextFrame.SetPixel(x, y, 255, 0, 0) # Red
				elif y < 5:
					nextFrame.SetPixel(x, y, 200, 200, 0) # Yellow
				else:
					nextFrame.SetPixel(x, y, 0, 200, 0) # Green

	return nextFrame

while True:
	randomHeights = numpy.empty([16])
	for i in range(len(tempXAxis)):
		x = tempXAxis[i]
		randomHeights[i] = (math.sin(randint(-3, 3) * x) + math.cos(randint(-3, 3) * x) + math.cos(randint(-3, 3) * x)) / 3

	ledMatrix.SwapOnVSync(drawFrame(randomHeights))
	time.sleep(0.1)
