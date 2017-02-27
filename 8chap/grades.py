class Grades(object):
	''' a mapping from student to a list of grades'''
	def __init__(self):
		self.students = []
		self.grades = {}
		self.isSorted = True

	def addStudent(self,student):
		'''assumes student is of type Student
		add student to the grade book'''
		if student in self.students:
			raise ValueError('Duplicate student')
		self.students.append(student)
		self.grades[student.getIdNum()] = []
		self.isSorted = False

	def addGrade(self,student,grade):
		''' assume grade is a float
			add grade to the list of grades for student'''
		try:
			self.grades[student.getIdNum()].append(grade)
		except:
			raise ValueError('student not in mapping')
	
	def getGrades(self,student):
		'''return the list of grades for student'''
		try:
			for g in self.grades[student.getIdNum()]:
				yield g
		except:
			raise ValueError('student not in mapping')

	def getStudents(self):
		'''return a list of students in the grade book'''
		if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		for s in self.students:
			yield s


def gradeReport(course):
	'''assume course i of type grades'''
	report = ''
	for s in course.getStudents():
		tot = 0.0
		numGrades = 0
		for g in course.getGrades(s):
			tot += g
			numGrades += 1
		try:
			average = tot/numGrades
			report = report + '\n' + str(s) + '\'s total grade is '+str(tot)+' and mean grade is '+str(average)
		except ZeroDivisionError:
			report = report + '\n' + str(s) +' has no grade.'

	return report


from MITPerson import *
if __name__ == '__main__':
	ug1 = UG('Jane Done',2014)
	ug2 = UG('John Done',2015)
	ug3 = UG('David Herry',2003)
	g1 = Grad('Billy Buckner')
	g2 = Grad('Buck F. Dent')
	sixHundred = Grades()
	sixHundred.addStudent(ug1)
	sixHundred.addStudent(ug2)
	sixHundred.addStudent(g1)
	sixHundred.addStudent(g2)
	for s in sixHundred.getStudents():
		sixHundred.addGrade(s,75)
	sixHundred.addGrade(g1,25)
	sixHundred.addGrade(g2,100)
	sixHundred.addStudent(ug3)
	print gradeReport(sixHundred)
