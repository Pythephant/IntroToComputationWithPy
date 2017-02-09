
def factI(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

def factR(n):
	if n <= 1:
		return 1
	else:
		return n * factR(n-1)


if __name__ == '__main__':
	print 'fact Iter:',factI(3)
	print 'fact Recur:',factR(3)
