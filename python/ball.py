#!/usr/bin/env python
import sys, time
import math

class Ball:
	gravity = -1 # Dots per second squared

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
		self.bounceOnEdge()

	def bounceOnEdge(self):
		if self.x < 0:
			self.vx = abs(self.vx)
			self.x = 0
		elif self.x > 31:
			self.vx = abs(self.vx) * -1
			self.x = 31

		if self.y < 0:
			self.vy = abs(self.vy)
			self.y = 0
		elif self.y > 15:
			self.vy = abs(self.vy) * -1
			self.y = 15

	def drawOnMatrix(self, matrix):
		matrix.SetPixel(int(self.x), matrix.height - 1 - int(self.y), self.r, self.g, self.b)

	def printValues(self):
		print "x: %.2f, y: %.2f - vx: %.2f vy: %.2f" % (self.x, self.y, self.vx, self.vy)