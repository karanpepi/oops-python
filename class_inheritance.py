# class animal:
# 	def eating(self):
# 		print("EATING")


# class dog(animal):
# 	def hunting(self):
# 		print("HUNTING")


# c1 = dog()
# c1.eating()


#another example

# class A:
# 	def __init__(self,name):
# 		self.name = name


# class B(A):
# 	def display(self):
# 		print(self.name)


# obj = B('python')
# obj.display()


# #Multilevel inheritance

# class grandfather:
# 	def display1(self):
# 		print("grandfather class")

# class father:
# 	def display2(self):
# 		print("father class")


# class child(grandfather,father):
# 	def display3(self):
# 		print("child class")


# obj = child()
# obj.display2()


#multiple inheritance

# class landanimal:
# 	def printing(self):
# 		print("This animal lives in on land")

# class water_animal:
# 	def display(self):
# 		print("this animal lives in water")

# class frog(landanimal,water_animal):
# 	pass


# f1 = frog()
# f1.printing()
# f1.display()




#Method overriding

# class A:
# 	def display(self):
# 		print("this is from class A")


# class B:
# 	def display(self):
# 		print("this is from class B")

# b = B()
# b.display()


#Encapsulation with private method

# class car:
# 	def __init__(self):
# 		self.__updatesoftware() #private method

# 	def drive(self):
# 		print("driving")

# 	def __updatesoftware(self):
# 		print("updating software")


# carobj = car()
# carobj.drive()
# # carobj.__updatesoftware() # can not be called



#Encapsulation with private variable

# class car:
# 	__maxspeed = 0
# 	__name = ""

# 	def __init__(self):
# 		self.__maxspeed = 200
# 		self.__name = "honda"

# 	def drive(self):
# 		print("driving")
# 		print(self.__maxspeed)

# 	def setspeed(self,speed):
# 		self.__maxspeed = speed
# 		print(self.__maxspeed)


# obj = car()
# obj.drive()
# obj.setspeed(300)
# obj.__maxspeed = 50 # value is not changed




#Polymorphism

# class dog:
# 	def sound(self):
# 		print("barking")

# class cat:
# 	def sound(self):
# 		print("Meow")


# def makesound(animal):
# 	animal.sound()



# catobj = cat()
# dogobj = dog()
# makesound(catobj)




#Use of super function

# class A:
# 	def __init__(self):
# 		print("CLASS A")

# class B(A):
# 	def __init__(self):
# 		print(super().__init__())
# 		print("CLASS B")


# objb = B()