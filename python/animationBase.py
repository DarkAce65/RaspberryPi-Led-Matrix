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
prevTime = time.clock()

try:
	print "Press Ctrl + C to stop executing"
	while True:
		nextFrame = ledMatrix.CreateFrameCanvas()
		ball.updateValues(time.clock() - prevTime)
		ball.drawOnMatrix(ledMatrix)
		prevTime = time.clock()
		ledMatrix.SwapOnVSync(nextFrame)
except KeyboardInterrupt:
	print "Exiting\n"
	sys.exit(0)