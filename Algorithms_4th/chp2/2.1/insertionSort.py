def insertionSort(arr):
	size = len(arr)
	i = 1
	for i in range(1,len(arr)):
		curr = arr[i]
		j = i-1
		while j >=0 and curr<arr[j]:
			temp = arr[j+1]
			arr[j+1] =arr[j]
			arr[j] = temp
			j-=1
		
	print(arr)


if __name__ == '__main__':
	a1 = [12,11,13,5,6]
	insertionSort(a1)