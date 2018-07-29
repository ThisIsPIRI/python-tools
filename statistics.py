def canBeMedianAfterInsert(data, toBeMedian, toBeInserted):
	halfLen = int(len(data) / 2)
	if len(data) % 2 == 0:
		if ((toBeInserted < data[halfLen - 1] and data[halfLen - 1] == toBeMedian) or
		(toBeInserted > data[halfLen] and data[halfLen] == toBeMedian) or
		(data[halfLen - 1] <= toBeInserted <= data[halfLen] and toBeInserted == toBeMedian)):
			return True
	else:
		if ((toBeInserted < data[halfLen - 1] and (data[halfLen - 1] + data[halfLen]) / 2 == toBeMedian) or
		(toBeInserted > data[halfLen + 1] and (data[halfLen] + data[halfLen + 1]) / 2 == toBeMedian) or
		(data[halfLen - 1] <= toBeInserted <= data[halfLen + 1] and (data[halfLen] + toBeInserted) / 2 == toBeMedian)):
			return True
	return False


def mode(data):
	"""Returns the mode(s) of data."""
	num = []; freq = [1]
	recorder = 0; maxFreq = 0
	def checkMax():
		if maxFreq < freq[recorder]:
			num.clear()
			maxFreq = freq[recorder]
			num.append(data[i - 1])
		elif maxFreq == freq[recorder]:
			num.append(data[i - 1])
	for i in range(1, len(data)):
		if data[i] != data[i - 1]:
			checkMax()
			recorder += 1
			freq.append(0)
		freq[recorder] += 1
	checkMax()
	return num
