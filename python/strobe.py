#!/usr/bin/env python
from rgbmatrix import RGBMatrix
import sys, time

rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)

height = ledMatrix.height
width = ledMatrix.width
on = 1
off = 1

try:
	print "Press Ctrl + C to stop executing"
	nextFrame = ledMatrix.CreateFrameCanvas()
	while True:
		nextFrame.Fill(255, 255, 255)
		nextFrame = ledMatrix.SwapOnVSync(nextFrame)
		time.sleep(on)
		nextFrame.Clear()
		nextFrame = ledMatrix.SwapOnVSync(nextFrame)
		time.sleep(off)
except KeyboardInterrupt:
	print "Exiting\n"
	sys.exit(0)