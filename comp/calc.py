def add(l):
	s=0
	for i in l:
		s+=i
	return s


def avg(l):
	a=0
	s1=0
	for i in l:
		s1+=i
	a=s1/len(l)
	return a


def relgrade():
	mx=float(input('enter highest marks:'))
	marks=float(input('enter your marks:'))
	
	if marks<= 0.35*mx:
		return 'D'
	elif marks>=0.36*mx and marks<= 0.5*mx:
		return 'C'
	elif marks>=0.51*mx and marks<=0.80*mx:
		return 'B'
	elif marks>=0.81*mx and marks <= 0.9*mx:
		return 'A'
	else:
		return 'S'

 	
		
	