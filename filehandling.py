#open and write to a file and read file

text = open("test.txt","w")
text.write("this is a test")
text.close() # to save changes to a files



import os

os.rename("test.txt","namechanged.txt")
os.remove("namechanged.txt")

os.mkdir("sample")
os.getcwd()
os.chdir()
os.listdir()


with open("test.txt") as fileobj:
	fileobj.write("this is with open we have written the text")