# Different elements
#zero indexing
#mutable (can be change/alter)
# E.g : [1,"python",1.23]
# Can be created using [] or list()
# List of list [[1,2],[4,5]]

list = [1,"python",1.23]
# for i in list:
# 	print(i)


#list comprehension
# items = [item for item in list if item=="python"]
# print(items)

#double list comprehension
# list2 = ["php",1,23.45]
# element =[i1 for i1 in list for i2 in list2 if i1==i2]
# print(element)


# #insert into list
# list.insert(2,"new inserted")
# print(list)


#sort operation can be perform on same datatype
# list3 = ["python","php","mysql"]
# list3.sort()
# print(list3)


#delete from list
# del list[1]
# print(list)


#append to list position in a list
# list.append("python")
# print(list)


#reverse the elements of list
# list.reverse()
# print(list)

#extend add one list to another
# fruits = ['apple', 'banana', 'cherry']

# cars = ['Ford', 'BMW', 'Volvo']
# fruits.extend(cars)

# print(fruits)


#copy of list
# newlist = list.copy()
# newlist[2]="karan"
# print(newlist)
# print(list)