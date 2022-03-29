class Rational:
	def __init__(self, numerator, denominator):
		gcd = self.gcd(numerator,denominator)
		self.numerator = numerator/gcd
		self.denominator = denominator/gcd

	def gcd(self,a,b):
		'''Use Euclid's algorithm to find greatest common dividor'''
		# always let a >=b
		if a <b:
			temp = a
			a = b
			b= temp
		
		while b>0:
			q = a//b
			r = a - q*b
			a = b
			b = r
			
		return a

	def __str__(self):
		return 'numerator: ' + str(self.numerator)+'& denominator: '+str(self.denominator)

	def plus(self, rational_num):
		return None

if __name__ == '__main__':
	r1 = Rational(27,33)
	print(r1)
	