import numpy as np
import matplotlib.pyplot as plt
import random
import struct


def writeImage(mat, width, height):
	writeAs = 'c'
	with open("test.ppm", 'wb') as f:
		f.write(bytes(f"P6\n{width} {height}\n255\n", 'utf-8'))
		for i in np.nditer(mat, order='C'):
			f.write(struct.pack(writeAs, bytes([i])))


def allRandom(width, height):
	format = 'c' #set to 'i' to repeat one R, one G, one B column and one empty column
	random.seed()
	with open("test.ppm", 'wb') as f:
		f.write(bytes(f"P6\n{width} {height}\n255\n", 'utf-8'))
		for i in range(width * height):
			f.write(struct.pack(format, bytes([random.randint(0, 255)])))
			f.write(struct.pack(format, bytes([random.randint(0, 255)])))
			f.write(struct.pack(format, bytes([random.randint(0, 255)])))


def prevRandom(width, height, vertical=False, zigzag=False, dotsDivisor=100, showProcess=True):
	"""Returns an np.ndarray of dimension (height, width, 3) representing an image of lines on which randomly and smoothly changing colors appear.
	vertical -- Whether to draw vertical lines instead of horizontal ones.
	zigzag -- Whether to continue the initial line in zigzag instead of making a new one for every row of pixels.
	dotsDivisor -- n in 1/n, the probability of a completely new color(dot) spawning instead of a slight diversion from the last one.
	Will disable dots if less than or equal to 0.
	showProcess -- Whether to show the process live through pyplot."""
	random.seed()
	
	mainAxis = width if vertical else height
	subAxis = height if vertical else width
	mat = np.empty((mainAxis, subAxis, 3), dtype=np.uint8)
	
	if showProcess:
		plt.ion()
		plt.figure(1)
		imgPlot = plt.imshow(mat)
		
	for i in range(mainAxis):
		goingReverse = zigzag and i % 2 == 1
		r = reversed(range(subAxis)) if goingReverse else range(subAxis)
		for j in r:
			if (dotsDivisor > 0 and random.randrange(0, dotsDivisor) == 0) or (j == 0 and not zigzag):
				for k in range(3):
					mat[i,j,k] = random.randint(0, 255)
			elif zigzag and (j == ((subAxis - 1) if goingReverse else 0)): # i will never be 0 if above if is False and zigzag is True
				for k in range(3):
					mat[i,j,k] = max(0, min(255, mat[i-1,j,k] + random.randint(-20, 20)))
			else:
				for k in range(3):
					mat[i,j,k] = max(0, min(255, mat[i,j+(1 if goingReverse else -1),k] + random.randint(-20, 20)))
					
		if showProcess:
			imgPlot.set_data(mat)
			plt.draw()
			plt.pause(0.001)

	if showProcess:
		plt.close()
	return np.transpose(mat, (1, 0, 2)) if vertical else mat


def neighborRandom(width, height, dotsDivisor=100):
	"""Returns an np.ndarray of dimension (height, width, 3) representing an image with pastel-like textures and colors.
	Set dotsDivisor to a negative number or 0 to disable random dots appearing throughout the image."""
	format = 'c'
	random.seed()
	mat = np.empty((height, width, 3), dtype=np.uint8)
	
	for i in range(height):
		for j in range(width):
			if (dotsDivisor > 0 and random.randrange(0, dotsDivisor) == 0) or (i == 0 and j == 0):
				for k in range(3):
					mat[i,j,k] = random.randint(0, 255)
			else:
				base = None
				if i == 0:
					base = mat[i][j - 1]
				elif j == 0:
					base = mat[i - 1][j]
				else:
					base = ((mat[i][j - 1] + mat[i - 1][j]) / 2).astype(np.int32) # Slightly faster than list comprehension.
				# TODO: fix a small number of dots appearing even when disabled
				for k in range(3):
					mat[i,j,k] = max(0, min(255, base[k] + random.randint(-20, 20)))			
	return mat


def main():
	width, height = [int(x) for x in input("Width and height(separated by a space): ").split()]
	divisor = 100 if input("dots?(y/n): ") == 'y' else -1
	if input("2d?(y/n): ") == 'y':
		writeImage(neighborRandom(width, height, divisor), width, height)
	else:
		writeImage(prevRandom(width, height, vertical=(input("vertical?(y/n): ") == 'y'),
			zigzag=(input("zigzag?(y/n): ") == 'y'),
			dotsDivisor=divisor, showProcess=(input("show process?(y/n): ") == 'y')), width, height)


if __name__ == "__main__":
	main()