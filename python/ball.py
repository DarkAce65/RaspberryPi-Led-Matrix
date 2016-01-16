#!/usr/bin/env python
import sys, time
import math

class Ball:
	gravity = -3 # Dots per second squared

	def __init__(self):
		self.r = 255
		self.g = 0
		self.b = 0

		self.x = 0
		self.y = 0
		self.vx = 0
		self.vy = 0

	def updateValues(self, timeElapsed=1):
		self.x += self.vx * timeElapsed
		self.y += self.vy * timeElapsed + 0.5 * Ball.gravity * timeElapsed ** 2
		self.vy += Ball.gravity * timeElapsed

	def drawOnMatrix(self, ledMatrix):
		ledMatrix.SetPixel(self.x, self.y, self.r, self.g, self.b)

	def printValues(self):
		print "x: %.2f, y: %.2f - vx: %.2f vy: %.2f" % (self.x, self.y, self.vx, self.vy)