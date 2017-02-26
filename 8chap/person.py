import datetime

class Person(object):
	def __init__(self,name):
		'''Create a person'''
		self.name = name
		try:
			lastBlank = name.rindex(' ')
			self.lastName = name[lastBlank+1:]
		except:
			self.lastName = name
		self.birthday = None

	def getName(self):
		'''return self's full name'''
		return self.name
	
	def getLastName(self):
		'''return self's last name'''
		return self.lastName

	def setBirthday(self,birthdate):
		'''Assume birthdate is of type datetime.date
		sets self's birthday to birthdate'''
		self.birthday = birthdate

	def getAge(self):
		'''return self's current age in days'''
		if self.birthday == None:
			raise ValueError
		return (datetime.date.today() - self.birthday).days

	def __lt__(self,other):
		if self.lastName == other.getLastName():
			return self.name < other.getName()
		return self.lastName < other.getLastName()

	def __str__(self):
		''' returns self's name'''
		return self.name


#test of the code
if __name__ == '__main__':
	me = Person('Micheal Guttag')
	him = Person('Barack Hussein Obama')
	her = Person('Madonna')
	print him.getLastName()
	him.setBirthday(datetime.date(1961,8,4))
	her.setBirthday(datetime.date(1958,8,16))
	print him.getName(),'is',him.getAge(),'days old'
	pList = [me,him,her]
	for p in pList:
		print p
	print 'pList sorted'
	pList.sort()
	for p in pList:
		print p
