"""WORK IN PROGRESS.
A script to fix a weird error that arose after a Windows update
where many(but not all) entries in the start menu were duplicated.
For example, (icon) Audacity -> (no icon) Audacity, (icon) Audacity (1)"""
import os
dir = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(dir)
num = 1
nameLength = "0" + str(int(math.log10(len(files))) + 1)
#todo make a recursive function
for f in files:
	if os.path.isfile(os.path.join(dir, f)):
		os.rename(f, format(num, "04") + '.png')
		num += 1
	elif os.path.isdir(os.path.join(dir, f)):
