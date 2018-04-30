import numpy as np
import random
import struct


def allRandom(width, height):
	format = 'c' #use 'i' to repeat one R, one G, one B column and one empty column
	random.seed()
	with open("test.ppm", 'wb') as f:
		f.write(bytes(f"P6\n{width} {height}\n255\n", 'utf-8'))
		for i in range(width * height):
			f.write(struct.pack(format, bytes([random.randint(0, 255)])))
			f.write(struct.pack(format, bytes([random.randint(0, 255)])))
			f.write(struct.pack(format, bytes([random.randint(0, 255)])))


def prevRandom(width, height, dotsDivisor=100):
	"""Set dotsDivisor to a negative number or 0 to disable colors randomly switching throughout the image."""
	format = 'c'
	random.seed()
	with open("test.ppm", 'wb') as f:
		f.write(bytes(f"P6\n{width} {height}\n255\n", 'utf-8'))
		prev = [None, None, None]
		for i in range(width * height):
			if (dotsDivisor > 0 and random.randrange(0, dotsDivisor) == 0) or prev[0] == None:
				for i in range(3):
					prev[i] = random.randint(0, 255)
					f.write(struct.pack(format, bytes([prev[i]])))
			else:
				for i in range(3):
					prev[i] = max(0, min(255, prev[i] + random.randint(-20, 20)))
					f.write(struct.pack(format, bytes([prev[i]])))
					
					
def neighborRandom(width, height, dotsDivisor=100):
	"""Set dotsDivisor to a negative number or 0 to disable random dots appearing throughout the image."""
	format = 'c'
	random.seed()
	with open("test.ppm", 'wb') as f:
		f.write(bytes(f"P6\n{width} {height}\n255\n", 'utf-8'))
		mat = np.empty((height, width, 3), dtype=np.uint8)
		for i in range(height):
			for j in range(width):
				if (dotsDivisor > 0 and random.randrange(0, dotsDivisor) == 0) or (i == 0 and j == 0):
					for k in range(3):
						mat[i,j,k] = random.randint(0, 255)
						f.write(struct.pack(format, bytes([mat[i,j,k]])))
				else:
					base = None
					if i == 0:
						base = mat[i][j - 1]
					elif j == 0:
						base = mat[i - 1][j]
					else:
						base = [int(x / 2) for x in mat[i][j - 1] + mat[i - 1][j]]
					for k in range(3):
						mat[i,j,k] = max(0, min(255, base[k] + random.randint(-20, 20)))
						f.write(struct.pack(format, bytes([mat[i,j,k]])))
			

def main():
	width, height = [int(x) for x in input("Width and height(separated by a space): ").split()]
	divisor = 100 if input("dots?(y/n): ") == 'y' else -1
	if input("2d?(y/n): ") == 'y':
		neighborRandom(width, height, divisor)
	else:
		prevRandom(width, height, divisor)
			
if __name__ == "__main__":
	main()