import copy

if __name__ == '__main__':
	a = [1,2,3]
	b = [4,5,6]
	l1 = [a,b]
	l2 = list(l1)
	l3 = copy.deepcopy(l1)
	print 'id(l1) == id(l2):',id(l1)==id(l2)
	print 'id(l1) == id(l3):',id(l1)==id(l3)
	print 'id(l1[0])==id(l2[0]):',id(l1[0])==id(l2[0])
	print 'id(l1[0])==id(l3[0]):',id(l1[0])==id(l3[0])
