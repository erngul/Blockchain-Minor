from calendar import c
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insertBeg(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
            self.tail = self.head
            return
        else:
            old_head = self.head
            self.head = Node(new_data)
            self.head.next = old_head
    # Insert at the end
    def insertEnd(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
            self.tail = self.head
            return
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(new_data)
            return
    # Insert after a node llist.insertAfter(2, 4)
    def insertAfter(self, data, new_data):
        if self.head == None:
            return
        current_node = self.head
        if current_node.data == data:
            nextNode = current_node.next
            current_node.next = Node(new_data)
            current_node.next.next = nextNode
            return
        while current_node.next != None or current_node.data == data:
            if current_node.data == data:
                nextNode = current_node.next
                current_node.next = Node(new_data,nextNode)
                return
            current_node = current_node.next  
    # Deleting a node at a specific index
    def deleteIndex(self, index):
        if index == 0:
            self.head = self.head.next
        count = 1
        current_node = self.head
        while current_node.next != None:
            if count == index:
                next_node = current_node.next.next
                current_node.next = next_node
                return
            current_node = current_node.next
            count += 1
    # Search an element
    def find(self, key):
        return -1
    # Sort the linked list
    def sort(self, head):
        pass
     # Print the linked list
    def printList(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next