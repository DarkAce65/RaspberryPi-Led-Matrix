#!/usr/bin/env python
import sys, time
import math

class Ball:
	gravity = -3 # Dots per second squared

	def __init__(self, x=0, y=0):
		self.r = 255
		self.g = 0
		self.b = 0

		self.x = 0
		self.y = 0
		self.vx = 0
		self.vy = 0

	def updateValues(self, timeElapsed=1): # timeElapsed in seconds
		self.x += self.vx * timeElapsed
		self.y += self.vy * timeElapsed + 0.5 * Ball.gravity * timeElapsed ** 2
		self.vy += Ball.gravity * timeElapsed

	def bounceOnEdge():
		if self.x < 0 or self.x > 16
			self.vx *= -1
		if self.y < 0 or self.y > 16
			self.vy *= -1

	def drawOnMatrix(self, ledMatrix):
		ledMatrix.SetPixel(int(self.x), ledMatrix.height - int(self.y), self.r, self.g, self.b)

	def printValues(self):
		print "x: %.2f, y: %.2f - vx: %.2f vy: %.2f" % (self.x, self.y, self.vx, self.vy)