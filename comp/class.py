'''
#classes and inheritance
class A:
	print('in class A')
	a=20
	b=40
class B(A):
	print('in class B')
	c=12
	d=10

#print(obj.a)
#print(obj.b)
#s=obj.a+obj.b
#single level inheritance

class C(B):
	print('in class C')
#multilevel inheritance 

obj=C()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)

print(s)

#multiple inheritance- one class from multiple classes

class A:
	print('in class A')
	a=20
	b=40
class B:
	print('in class B')
	c=12
	d=10

class C(A,B):
	print('in class C')

ob=C()
print(ob.a, ob.c)
'''
class add:
	a=10
	b=20
	def add1(self):
		s=self.a+self.b
		print('sum=',s)

class sub(add):
	a=10
	b=20
	def sub1(self):	
		mi=self.b-self.a
		print('subtratction=',mi)


class mul(sub):
	a=10
	b=20
	def mul1(self):	
		m=self.a*self.b
		print('multiplication=',m)


ob=mul()
ob.add1()
ob.sub1()
ob.mul1()

















