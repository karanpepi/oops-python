

a = -1

try:
	if a<0:
		raise Exception
except Exception as e:
	print("This is error:{}".format(e))
