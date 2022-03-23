class Counter:

	def __init__(self):
		self.num=0

	def increase(self):
		self.num+=1

	def display(self):
		return self.num


def binarySearch(array,value,couter):

	low = 0
	high = len(array) -1
	res = False
	while (low<=high):
		
		mid = low + (high-low)//2
		couter.increase()
		if value==array[mid]:
			res=True
			break
		if value> array[mid]:
			low=mid+1
		if value < array[mid]:
			high=mid-1
	print(couter.display())
	return res


if __name__ == '__main__':
    a1 = [1,4,5,6,7,67]
    t1= 1
    c1 = Counter()

    print(binarySearch(a1,t1,c1))