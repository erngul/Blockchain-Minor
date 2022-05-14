from Node import *

A = Node('A')

B = Node()
B.setData('B')

print(A)
print(B)

print(A.getData())
print(A.getNext())

A.setNext(B)
tmp = A.getNext()
print(tmp.getData())

print(B.getNext())