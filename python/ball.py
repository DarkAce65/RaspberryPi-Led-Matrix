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

	def updateValues(self):
		self.x += self.vx
		self.y += self.vy
		self.vy += gravity

	def drawOnMatrix(self, ledMatrix):
		ledMatrix.SetPixel(self.x, self.y, self.r, self.g, self.b)