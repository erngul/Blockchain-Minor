class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning of the list
    def insertBeg(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        oldHead = self.head
        self.head = Node(new_data)
        self.head.next = oldHead
    
    # Insert at the end
    def insertEnd(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = Node(new_data)

    # Insert after a node
    def insertAfter(self, data, new_data):
        if self.head is None:
            return
        current_node = self.head
        if current_node.data == data:
            nextNode = current_node.next
            current_node.next = Node(new_data)
            current_node.next.next = nextNode
            return
        while current_node.next != None or  current_node.data == data:
            if current_node.data == data:
                nextNode = current_node.next
                current_node.next = Node(new_data)
                current_node.next.next = nextNode
                return
            current_node = current_node.next


    # Deleting a node at a specific index
    def deleteIndex(self, index):
        if index == 0:
            self.head = self.head.next
        indexCount = 1
        current_node = self.head
        while current_node.next != None:
            if indexCount == index:
                nextNode = current_node.next.next
                current_node.next = nextNode
                return
            current_node = current_node.next
            indexCount += 1


    # Search an element
    def find(self, key):
        current_node = self.head
        count = 0
        while current_node != None:
            if current_node.data == key:
                return count
            count += 1
            current_node = current_node.next
        return -1

    # Sort the linked list
    def sort(self, head):
        values = []
        current_node = head
        while current_node != None:
            values.append(current_node.data)
            current_node = current_node.next

        values.sort()
        self.head = Node(values[0])
        for val in values[1:]:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(val)


    # Print the linked list
    def printList(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
        print("\n")