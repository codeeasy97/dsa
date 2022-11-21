# Construct a Linked list
# 1. insert - insert at head - insert at tail - insert at position
# 2. print

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertAtTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertAtHead(self, data):
        new_node = Node(data)
        #base case
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    
    def insertAtPosition(self, data, position):
        new_node = Node(data)
        count = 1
        head = self.head
        temp = self.head
        while count < position -1:
            self.head = self.head.next
            count = count + 1
        temp = self.head
        new_node.next = temp.next
        temp.next = new_node
        self.head = head

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
llist.insertAtTail(1)
llist.insertAtTail(2)
llist.insertAtTail(3)
llist.insertAtTail(4)
llist.insertAtTail(5)
llist.insertAtTail(6)

# llist.insertAtHead(7)
print("Given linked list:")
llist.printList()
print("\n")
llist.insertAtPosition(100,3)

print("linked list after insert at pos:")
llist.printList()
print("\n")