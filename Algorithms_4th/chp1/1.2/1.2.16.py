class Rational:
	def __init__(self, numerator, denominator):
		gcd = self.gcd(numerator,denominator)
		self.numerator = numerator/gcd
		self.denominator = denominator/gcd

	def gcd(self,a,b):
		'''Use Euclid's algorithm to find greatest common dividor'''
		# always let |a| >=|b|
		a = abs(a)
		b = abs(b)
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
		return str(self.numerator)+'/'+str(self.denominator)

	def plus(self, rational_num):
		new_denom = self.denominator*rational_num.denominator
		new_nom = self.numerator*rational_num.denominator + rational_num.numerator*self.denominator
		return Rational(new_nom,new_denom)

	def minus(self, rational_num):
		new_denom = self.denominator*rational_num.denominator
		new_nom = self.numerator*rational_num.denominator - rational_num.numerator*self.denominator
		return Rational(new_nom,new_denom)

	def times(self, rational_num):
		new_denom = self.denominator*rational_num.denominator
		new_nom = self.numerator*rational_num.numerator
		return Rational(new_nom,new_denom)

	def divides(self, rational_num):
		new_denom = self.denominator*rational_num.numerator
		new_nom = self.numerator*rational_num.denominator
		return Rational(new_nom,new_denom)

	def equals(self, rational_num):
		return (self.denominator==rational_num.denominator) and (self.numerator==rational_num.numerator)



if __name__ == '__main__':
	r1 = Rational(27,33)
	r2 = Rational(54,66)
	r3 = Rational(1,3)
	r5 = Rational(2,3)
	print(r3.plus(r1))
	print(r2.equals(r1))
	print(r1.equals(r3))
	print(r1.minus(r2))
	print(r1.times(r3))
	print(r5.plus(r3))
	print(r3.divides(r5))
	