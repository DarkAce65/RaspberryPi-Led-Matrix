#!/usr/bin/env python
from rgbmatrix import RGBMatrix
import sys, time
from ball import Ball

rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)

numRows = 16
height = ledMatrix.height
width = ledMatrix.width
ball = Ball()

try:
	print "Press Ctrl + C to stop executing"
	while True:
		nextFrame = ledMatrix.CreateFrameCanvas()
		ball.updateValues(0.1)
		ball.drawOnMatrix(nextFrame)
		ledMatrix.SwapOnVSync(nextFrame)
		time.sleep(0.1)
except KeyboardInterrupt:
	print "Exiting\n"
	sys.exit(0)