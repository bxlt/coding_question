def readInts(filename):
	file = open(filename,'r')
	res = []
	line = file.read()
	words = line.split()
	for word in words:
		res.append(int(word))
	return res
