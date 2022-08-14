'''
class A:
	x='cse'
	def f1()

a=A()
b=A()
#print(a.x)    #cse
#print(b.x)
#print(A.x)

a.x='mech'
print(a.x)     #mech
A.x='ece'

print(a.x)    
print(b.x)
print(A.x)           
'''

class A:
	stat=10
	def __init__(self,i):
		self.i=i
	def f1(self):
		print('for objects')
		print(self.i)

	@staticmethod            #access only static variables
	def f2():
		print('for class-cannot access static')
		print(A.stat)
		#print(a1.i)
		print(self.i) #error-self not available


a1=A(0)
a2=A(1)

a1.f1()
A.f2()
a1.f2()
print(A.stat)
print(a1.stat)

















