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

numRows = 16
height = ledMatrix.height
width = ledMatrix.width
barWidth = width / numRows
tempXAxis = numpy.empty([numRows])
for i in range(numRows):
	tempXAxis[i] = i * pi / numRows

try:
	print "Press Ctrl + C to stop executing"
	while True:
		nextFrame = ledMatrix.CreateFrameCanvas()
		barHeights = numpy.empty([numRows])
		for i in range(len(tempXAxis)):
			x = tempXAxis[i]
			barHeights[i] = (math.sin(randint(-3, 3) * x) + math.cos(randint(-3, 3) * x) + math.cos(randint(-3, 3) * x)) / 3

		for x in range(width):
			barHeight = int(barHeights[int(x / barWidth)] * height)
			for y in range(height):
				if height - y <= barHeight:
					if y < 2:
						nextFrame.SetPixel(x, y, 255, 0, 0) # Red
					elif y < 5:
						nextFrame.SetPixel(x, y, 200, 200, 0) # Yellow
					else:
						nextFrame.SetPixel(x, y, 0, 200, 0) # Green

		ledMatrix.SwapOnVSync(nextFrame)
		time.sleep(0.1)
except KeyboardInterrupt:
	print "Exiting\n"
	sys.exit(0)