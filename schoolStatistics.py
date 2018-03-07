"""
A script to solve a statistics problem I found interesting a while back in school.
Requires canBeMedianAfterInsert() function in statistics module. An implementation is available in statistics.py.
"""
from statistics import canBeMedianAfterInsert
print("We're going to insert number a to an array so a is the mode and the median is a + ", end="")
addend = int(input())
print("Input an array : ")
data = [int(x) for x in input().split()]
data.sort()
num = []; freq = []
num.append(data[0])
freq.append(1)
recorder = 0; maxFreq = 1
for i in range(1, len(data)):
	if data[i] != data[i - 1]:
		if maxFreq < freq[recorder]:
			maxFreq = freq[recorder]
		recorder += 1
		num.append(data[i])
		freq.append(0)
	freq[recorder] += 1
candidates = []
for i in range(len(num)):
	if freq[i] + 1 >= maxFreq:
		candidates.append(num[i])
halfLen = int(len(data) / 2)
for c in candidates:
	if canBeMedianAfterInsert(data, c + addend, c):
		print(c)
