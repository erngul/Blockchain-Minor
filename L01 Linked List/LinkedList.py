class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data
        
    def setNext(self,next):
        self.next = next

class LinkedList:    

    def __init__(self):
        self.first = None

    def append(self, item):
        # This method should append an item to the end of the list
        if self.first is None:
            self.first = item
            return
        current_node = self.first
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = item

    def getLen(self):
        # This method should find the length of the list and return it
        if self.first is None:
            return 0
        counter = 1
        current_node = self.first
        while current_node.next != None:
            current_node = current_node.next
            counter += 1
        return counter

    def printAll(self):
        # This method should print all elements in the list from the head to the end
        if self.first is None:
            print(0)
            return
        current_node = self.first
        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next
