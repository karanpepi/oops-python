
#dictonary key value pair
#can take multiple type of values
#we can change the dictionary values
#dict.items,dict.values,dict.keys we can access the values,key and key,value both
# Dictionary can be created using dict constructor

a = {}

# a['1']="one"
# a['2']="two"
# print(a)
# value = a.get('3',"sadasd")
# print(value)

# items = [i for i in a.items()]
# print(items)


#fromkeys create a dictionary with specified key and values
keys = {"1",2,3}
values = {"php","python","nodjes"}
dict = a.fromkeys(keys,values)
print(dict)