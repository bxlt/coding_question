# Original O(n^2)
def find_pairs(filename):
	file = open(filename ,'r')
	contents = file.read().split()
	res = 0
	for i in range(len(contents)):
		for j in range(i+1,len(contents)):
			if contents[i]==contents[j]:
				res+=1

	file.close()
	return res

# Optimized O(nlogn) assume using merge sort
def opt_find_pairs(filename):
	file = open(filename ,'r')
	contents = file.read().split()
	res = 0
	#sort number
	contents.sort()
	i = 0
	size = len(contents)
	while i < size-1:
		if contents[i] ==contents[i+1]:
			res+=1
		i+=1
	return res
