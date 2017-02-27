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

	def isStudent(self):
		return isinstance(self,Student)
	

class Student(MITPerson):
	pass

class UG(Student):
	def __init__(self,name,classYear):
		MITPerson.__init__(self,name)
		self.year = classYear

	def getClass(self):
		return self.year

class Grad(Student):
	pass

class TransferStudent(Student):
	def __init__(self,name,fromSchool):
		MITPerson.__init__(self,name)
		self.fromSchool = fromSchool
	def getOldSchool(self):
		return self.fromSchool
	
#test of hte code
if __name__ == '__main__':
	p1 = MITPerson('Mark Guttag')
	p2 = MITPerson('Billy Bob Beaver')
	p3 = MITPerson('Billy Bob Beaver')
	p4 = Person('Billy Bob Beaver')
	'''
	print 'p1 < p2 = ',p1<p2
	print 'p3 < p2 = ',p3<p2
	print 'p4 < p1 = ',p4<p1
	print 'p1 < p4 = ',p1<p4
	'''
	p5 = Grad('Buzz Aldrin')
	p6 = UG('Billy Beaver',1984)
	'''print p5 ,'is a graduate stutent is',type(p5)==Grad
	print p5,'is a undergraduate stutent is',type(p5)==UG
	print p6,'is a undergraduate stutent is',type(p6)==UG'''
	print p5,'is a student is',p5.isStudent()
	print p6,'is a student is',p6.isStudent()
	print p3,'is a student is',p3.isStudent()
