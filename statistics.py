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


def mode(data, isSorted=False):
	"""Returns the mode(s) of data. Set sorted to True if data is sorted. The order doesn't matter."""
	result = []; maxFreq = 0; freq = 0; lastNum = None
	if not isSorted: data = sorted(data)
	
	for num in data:
		if num != lastNum:
			if freq > maxFreq:
				result.clear()
			if freq >= maxFreq:
				result.append(lastNum)
				maxFreq = freq
			freq = 0
			lastNum = num
		freq += 1

	lastNum = data[len(data) - 1]
	# TODO: make this a function
	if freq > maxFreq:
		result.clear()
	if freq >= maxFreq:
		result.append(lastNum)
		maxFreq = freq
	return result
