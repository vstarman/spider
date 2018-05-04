# data = range(10)


# funcs = []
# for i in data:
#    	l = lambda x: i * x
#    	funcs.append(l)
   
#    	def m(x):
#    		return i * x

#    	funcs.append(m)

# i = 21
# for func in funcs:
# 	print func(2)

# def baz(x, i=i):
# 	return i * x



def func():
	l = list()
	for i in range(10):
		def func2(x):
			return i * x
		l.append(func2)
	return l


for i in func():
	print(i(2))


# data = range(10)

# funcs = (lambda x: i*x for i in data)

# i = 12345
# for func in funcs:
#     print(func(2))

# (for i in range(10))