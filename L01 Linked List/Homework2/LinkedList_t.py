from LinkedList import *

llist = LinkedList()

llist.insertEnd(1) # Linked List: 1 
llist.insertBeg(2) # Linked List: 2 1
llist.insertBeg(3) # Linked List: 3 2 1
llist.insertEnd(4) # Linked List: 3 2 1 4

llist.insertAfter(2, 4)     # This call will insert 4 after the first occurrence 2 (if there are more than one 2)
                            # Linked List: 3 2 4 1 4
llist.insertAfter(4, 5)     # This call will insert 6 after the first occurrence 4 (if there are more than one 2)
                            # Linked List: 3 2 4 6 1 4

llist.printList()

# Delete item at position 2 (3rd element) (list starts from position 0) 
llist.deleteIndex(2)
llist.printList()

item_to_find = 2
index = llist.find(item_to_find)
if index !=-1:
    print(str(item_to_find) + " is at index: " + str(index))
else:
    print(str(item_to_find) + " is not found ")

llist.sort(llist.head)
llist.printList()