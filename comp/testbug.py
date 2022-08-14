#wap to print list after removing the 0th, 6yh, 7th numbers in list
'''
l=[0,1,2,3,4,5,6,7,8,9]
l1=[l[i] for i in range(len(l)) if i not in (0,6,7)]
print(l1)
'''

#wap to print list after removing the value 25
l=[10,20, 25, 30, 25, 40]
l1=[l[i] for i in range(len(l)) if l[i]!=25]
print(l1)