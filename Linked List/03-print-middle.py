# print middle of the linked list
#1. size approach
#2. two pointer approach

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last  = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    def getCount(self):
        temp = self.head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        return count

    def printMiddleOne(self, size):
        start = 1
        mid = size//2
        while start <= mid:
            self.head = self.head.next
            start = start + 1
        print("Middle Element :", self.head.data)
    
    def printMiddleTwo(self):
        slow = fast = self.head
        while fast.next:
            if fast.next.next is not None:
                fast = fast.next.next
            else:
                break
            slow = slow.next
        print("Middle Element 2 pointer: ",slow.data)

llist = LinkedList()
llist.push(1) #slow fast
llist.push(2) #1 slow
llist.push(3) #1 fast, 2 slow
llist.push(4)
llist.push(5) #2 fast
print("\n")
llist.printList()
print("\n")
size = llist.getCount()
print("\n")
llist.printMiddleOne(size)
# llist.printMiddleTwo()