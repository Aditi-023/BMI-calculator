import calc

l=[]
for i in range(3):
	x=int(input('enter marks:'))
	l.append(x)



su=calc.add(l)
av=calc.avg(l)
grade=calc.relgrade()

print('Sum=', su)
print('average=', av)
print('Relative grade=', grade)
	