def isRotation(s1,s2):
	# compare same length
	len1 = len(s1)
	len2 = len(s2)
	if len1!=len2:
		return False
	temp = s1+s1
	# print(temp)
	res = s2 in temp
	return res

a='ACTGACG'
b='TGACGAC'
print(isRotation(a,b))