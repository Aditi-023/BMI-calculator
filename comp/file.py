'''
f=open('a.txt', 'r')
rd=f.readlines()
print(rd)
f.close()

f=open('b.txt', 'w')
f.write('this sucks ass')
print('what the hell', file=sys.stdout)
f.close()
'''
n=0
f=open('b.txt', 'r')
rd=f.readlines()
for i in rd:
   n+=i.count('python')
print(n)
f.close()