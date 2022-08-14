import a1
print('module a2')
# op: module 1 30 module a2
from a1 import *
print('module a2')

import a1
print(a1.a) #will show error otherwise

from a1 import a
print(a) #need not include a1.
print(b) #error; didnt import b

import a,b #imports both
print(a,b)

import a1, a3
print('in b2')
#op: in module a1 30 module 3 in b2

import a3
#op: module a3


import a3
print(a3.x) #op: without a3. it will throw error
print(a3.y)
print(a3.sum)


#alias names for modules
import a3 as ali
print(ali.x)
print(ali.y)
print(ali.sum)
#op: 300 100 200 300


import a3
print(__name__)
#op: module a3 (from a3); a3(executed in a2);   __main__ ( from a3, a2 is main)