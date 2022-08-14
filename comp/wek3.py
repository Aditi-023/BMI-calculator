'''
#1. Write a program to read four characters seperately from the user and covert it to the next alphabet.

a=input('a=')
b=input('b=')
c=input('c=')
d=input('d=')

a1=chr(ord(a)+1)
b1=chr(ord(b)+1)
c1=chr(ord(c)+1)
d1=chr(ord(d)+1)

print(a1, b1, c1, d1)



# 2. Write a program to swap the contents of two memory locations using bitwise operator. (No temporary variables or arithmatic operators.)


a=int(input('enter value 1: '))
b=int(input('enter value 2: '))
print('values before swapping:')
print('a=', a)
print('b=', b)

a=a^b
b=a^b
a=a^b
print('values after swapping:')
print('a=', a)
print('b=', b)





# 3.write a python program to clear right-most set bit of a number

n=int(input('enter a number:'))

if n%2!=0:
 n-=1
 print('reset number:', n)
else:
 print('reset number:', n)




# 4. Write a python program to perform multiplication of two random float values.


import random
x=random.random()
y=random.random()
res=x*y
print('x=', x)
print('y=', y)
print('Result:', res)




# 5. Write a python program to perform multiplication of two random float values in a range of 10.5 to 20.5


import random
x=random.uniform(10.5, 20.5)
y=random.uniform(10.5, 20.5)
res=x*y
print('x=', x)
print('y=', y)
print('Result:', res)



# 6. Write a program to generate same random number everytime.


import random
random.seed(10)
x=random.randint(10,20)
print('x=', x)



# 7. Roll a dice in such a way that every time you get the same number.


import random as r
x=[1,2,3,4,5,6]
r.seed(567)
x=r.choice(x)
print('random number x:', x)




  8. Write a program to
     a) shuffle students in a class. Assuming number of students are ten.
     b) Choose 1 student.
     c) Create a random sample of size 2, and 4, from the available number of population who are candidates to become event  coordinators.


import random as r
x=[1,2,3,4,5,6,7,8,9,10]

r.shuffle(x)
print('shuffled class:', x)

y=r.choice(x)
print('choice of one student:', y)

print('random sample of 2:', r.sample(x,2))
print('random sample of 4:', r.sample(x,4))











# 9. Write a program to get a random character from a specified string.


import random as r
p='computer'
print('random character:', r.choice(p))

 




# 10. Suppose a person wants to calculate the simple interest for the account he has taken for specified number of years.(read the values from user)


p=int(input('enter principle amount:'))
t=int(input('enter the number of years:'))
r=int(input('enter interest rate:'))
I=(p*r*t)/100
print('the interest for', t, ' years is', I)




# 11. Write a Python program which accepts the radius of a sphere and computes the volume. What is the volume and surface area of a sphere? The volume of a sphere with radius r is 4/3 πr3 .

r=int(input('enter radius:'))

v=(12.5*r*r)/3
a=4*3.14*r*r

print('Volume of sphere:', v)
print('Area of sphere:', a)





# 12.Python Program to Find the Gravitational Force Acting Between Two Objects



m1=float(input('enter m1:'))
m2=float(input('enter m2:'))
r=float(input('enter r:'))
g=667*10**-13
f=(g*m1*m2)/r*r
print('force is: ', f)



# 13.Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the rst copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?


dis=24.95-(0.4*24.95)
a=dis+3
b=(0.75+dis)*59
s=a+b
print('cost of book ($24.95) after discount: ', dis)
print('cost of 60 books after shipping fee: ', s)






# 14. If person leave house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do the person get home for breakfast?



srt=6+(52/60)
ep=(8+(15/60))/60
tp=(7+(12/60))/60
total=2*ep + tp
b=srt+total
min=(b-int(b))*60
print('hour: ', b)
print('minute: ', min)






# 15. Write a program to:
      A) To calculate wind chill index.
      B) To Convert radian to degree.
      C)To calculate distance between two points using latitude and longitude.
      D)Write a program
       1) To round the value of -4.3 and then takes the absolute value of that result.
       2) That takes the ceiling of sine of 34.5.
       3) To produces the floor of -2.8.
'''





import math

t=float(input('enter temperature(F):'))
w=float(input('enter wind speed(mph):'))
sol=35.74 + 0.6215*t - 35.75*w**0.16 + 0.4275*w**0.16
print('wind chill index is: ', sol)


rad=float(input('enter radians:'))
deg=rad*57.296
print('the degrees are: ', deg)

from math import radians, sin, cos, acos
R=6373.0

la1=radians(float(input('enter latitude 1:')))
la2=radians(float(input('enter latitude 2:')))
lo1=radians(float(input('enter longitude 1:')))
lo2=radians(float(input('enter longitude 2:')))


dla=la2-la1
dlo=lo2-lo1
dist=R* acos(sin(la1)*sin(la2) + cos(la1)*cos(la2)*cos(lo1-lo2))

print('The distance is:', dist)



a=round(-4.3)
print('absolute value of -4.3:', abs(a))



x=math.sin(34.5)
print('ceiling value of x:', math.ceil(x))



print('floor of 2.8:', math.floor(2.8))






































