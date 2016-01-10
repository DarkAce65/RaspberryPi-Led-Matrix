#!/usr/bin/env python
from rgbmatrix import RGBMatrix
from random import randint
import time

rows = 16
chains = 1
parallel = 1
ledMatrix = RGBMatrix(rows, chains, parallel)
height = ledMatrix.height
width = ledMatrix.width
nextFrame = ledMatrix.CreateFrameCanvas()

while True:
	nextFrame.SetPixel(randint(0, width), randint(0, height), randint(0, 255), randint(0, 255), randint(0, 255))
	nextFrame = ledMatrix.SwapOnVSync(nextFrame)