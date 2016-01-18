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
	while True:
		ledMatrix.Fill(255, 255, 255)
		time.sleep(on)
		ledMatrix.Clear()
		time.sleep(off)
except KeyboardInterrupt:
	print "Exiting\n"
	sys.exit(0)