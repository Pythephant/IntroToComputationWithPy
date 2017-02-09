def fib(n):
	global counts
	counts += 1
	if n < 0 :
		return 0
	elif n == 1 or n == 0 :
		return 1
	else:
		return fib(n-1) + fib(n-2)

def testFib(n):
	for i in range(n):
		global counts
		counts = 0
		print 'fib of',i,'=',fib(i)
		print 'counts of fibs,',counts

if __name__ == '__main__':
	global counts 
	counts = 0
	print fib(20)
	print counts

