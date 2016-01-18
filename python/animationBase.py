#!/usr/bin/env python
from rgbmatrix import RGBMatrix
import sys, time
from ball import Ball

rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)

height = ledMatrix.height
width = ledMatrix.width
red = Ball(5, 9, 7)
green = Ball(2, 12, 4, -4, 0, 255, 0)
blue = Ball(6, 9, 15, 12, 0, 0, 255)

try:
	print "Press Ctrl + C to stop executing"
	while True:
		nextFrame = ledMatrix.CreateFrameCanvas()
		red.updateValues(1 / 60.0)
		green.updateValues(1 / 60.0)
		blue.updateValues(1 / 60.0)
		red.drawOnMatrix(nextFrame)
		green.drawOnMatrix(nextFrame)
		blue.drawOnMatrix(nextFrame)
		ledMatrix.SwapOnVSync(nextFrame)
		time.sleep(1 / 60.0)
except KeyboardInterrupt:
	print "Exiting\n"
	sys.exit(0)