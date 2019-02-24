#Instance Method and class method


class Student:

	school = "IES" #class variable

	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return (self.m1+self.m2+self.m3) / 3


	def school_info(self):
		return self.school

	@staticmethod # this method does not depend on instance or class variable
	def static_example(): #no self parameter pass here
		return 1

s1 = Student(23,34,45)
s2 = Student(45,44,67)

print(s1.avg())
print(s2.avg())
# print(Student.school)
print(s1.school_info())
a = Student.static_example
print(a)