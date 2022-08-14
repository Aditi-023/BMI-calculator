'''
class A:
	def display(self):
		print('this is class A')

class B:
	def display(self):
		print('this is class B')

a1=A()
b1=B()

def f1(x):
	x.display()

f1(a1)
f1(b1)
'''

class A:
	def fun(self):
		print("A")

class B(A):                         #local one has priority
	def fun(self):
		print('B')

b=B()
b.fun()


















