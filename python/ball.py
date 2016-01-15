#!/usr/bin/env python
from rgbmatrix import RGBMatrix
import sys, time
import math

rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)

numRows = 16
height = ledMatrix.height
width = ledMatrix.width

try:
	print "Press Ctrl + C to stop executing"
	while True:
		nextFrame = ledMatrix.CreateFrameCanvas()
		ledMatrix.SwapOnVSync(nextFrame)
except KeyboardInterrupt:
	print "Exiting\n"
	sys.exit(0)