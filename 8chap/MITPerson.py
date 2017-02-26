from person import Person

class MITPerson(Person):
	nextIdNum = 0 #identification number

	def __init__(self,name):
		Person.__init__(self,name)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1
	
	def getIdNum(self):
		return self.idNum

	def __lt__(self,other):
		return self.idNum < other.getIdNum()
	

#test of hte code
if __name__ == '__main__':
	p1 = MITPerson('Mark Guttag')
	p2 = MITPerson('Billy Bob Beaver')
	p3 = MITPerson('Billy Bob Beaver')
	p4 = Person('Billy Bob Beaver')

	print 'p1 < p2 = ',p1<p2
	print 'p3 < p2 = ',p3<p2
	print 'p4 < p1 = ',p4<p1
	print 'p1 < p4 = ',p1<p4
