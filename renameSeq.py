"""A script to rename a sequence of image files whose members don't have ascending integers as names
but do have lexicographically ascending names so they can be compiled into a video with VirtualDub."""
import os
import math
dir = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(dir) #TODO: make sure the files are sorted by ascending lexicographical order of their names.
num = 1
nameLength = "0" + str(int(math.log10(len(files))) + 1)
for f in files:
	if os.path.isfile(os.path.join(dir, f)):
		os.rename(f, format(num, nameLength) + '.png')
		num += 1
