def findDivisors(n1,n2):
	'''Assume n1 and n2 are positive ints
	returns a tuple containing all the common divisors of n1 and n2'''
	divisors = ()
	for i in range(1,min(n1,n2)+1):
		if n1 % i == 0 and n2 % i == 0:
			divisors = divisors + (i,)
	return divisors

def findExtremeDivisors(n1,n2):
	'''Assume n1 and n2 are positive ints
	returns the minDivisor (>1) and the max Divisor'''
	divisors = ()
	maxD,minD = None,None
	for i in range(2,min(n1,n2)+1):
		if n1%i == 0 and n2%i == 0:
			if minD == None or i < minD:
				minD = i
			if maxD == None or i > maxD:
				maxD = i
	return minD,maxD

#test
if __name__ == '__main__':
	print findExtremeDivisors(5,6)
	print findExtremeDivisors(3,6)
	print findExtremeDivisors(12,6)
