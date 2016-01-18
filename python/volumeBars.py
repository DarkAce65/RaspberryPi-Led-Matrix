#!/usr/bin/env python
from rgbmatrix import RGBMatrix
from random import randint
import sys, time
import numpy, math

pi = numpy.pi
rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)

numBars = 16
height = ledMatrix.height
width = ledMatrix.width
barWidth = width / numBars
tempXAxis = numpy.empty([numBars])
for i in range(numBars):
	tempXAxis[i] = i * pi / numBars

try:
	print "Press Ctrl + C to stop executing"
	while True:
		nextFrame = ledMatrix.CreateFrameCanvas()
		barHeights = numpy.empty([numBars])
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