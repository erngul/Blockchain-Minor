from LinkedList import *

new_node = Node()
new_node.setData('A')

llst1 = LinkedList()
llst1.append(new_node)
llst1.printAll()
print(llst1.getLen())

new_node = Node('B')
llst1.append(new_node)
llst1.printAll()
print(llst1.getLen())

for item in ['C', 'D', 'E', 'F']:
    new_node = Node(item, None)
    llst1.append(new_node)    

llst1.printAll()
print(llst1.getLen())