'''
a='python'
print('{0:10} programming'.format(a))
print('{0:10} programming'.format(44))
'sam has {0:d} red balls and {0:d} yellow balls'.format(10,20) #d=integer
'''
for i in range(1,4):
	for j in range(1,4):
		if(i==j):
			print(1, end='')
		else:
			print(0, end='')
	print()
	
		







'''
#list comprehension
#create a list containing a string 'hello' 5 times.
print(['hello' for x in range(5)])

#print square of numbers from 1 to 5
print([i*i for i in range(1,6)])

#print list of tupples having number and square/cube from 1 to 5
print([(i,i**3) for i in range(1,6)])

#list of strings and its length
print([(i,len(i)) for i in ['hello', 'what', 'apple', 'cool']])

#list of string input. print in upper case
print([i.upper() for i in ['hello', 'this', 'is', 'python']])

#print all words from list whose length exceeds 5
print([i.upper() for i in ['heyyyy', 'hell', 'apples', 'cool'] if len(i)>5])

#list
l=[1,7,-6,-2,5,-9,12,-23,32,67]
print([-i for i in l if i<0])
'''
#list l1
l1=[1,2,3,4]
l2=[5,6,7,8]
print([x+y for x, y in zip(l1,l2)])