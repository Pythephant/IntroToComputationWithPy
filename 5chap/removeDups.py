def removeDups(l1,l2):
	for e1 in l1:
		if e1 in l2:
			l1.remove(e1)

def removeDups(l1,l2):
	newL = list(l1)
	for i in newL: 
		if i in l2:
			l1.remove(i)

if __name__ == '__main__':
	l1 = [1,2,3,4]
	l2 = [1,2,5,6]
	removeDups(l1,l2)
	print 'l1 =',l1
