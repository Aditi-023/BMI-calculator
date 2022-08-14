a=10
b=3
#b=0
'''
try:
	c=a/b

#except ZeroDivisionError:    #inbuilt error
except:                       #any error wrt to this will print same print statement
	print('Traceback(most recent call last):')
	print('   error: Zero division')
else:
	print(c)
finally:
	print('this is exception handling')

'''
try:
	c=b-a
	assert b!=3, "not allowed"

except:                       
	print('   error: Zero division')
else:
	print(c)
finally:
	print('this is exception handling')