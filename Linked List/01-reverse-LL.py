class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None


    def push(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = temp

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
# step- 6:
# prev = 5
# curr=6
# next = None
# curr.next = 5
# prev = 6
# curr = None

# step7:
# prev = 6
# curr = None

# step-5:
# prev = 4
# curr = 5
# next = 6
# curr.next = 4
# prev = 5
# curr = 6

# step-4:
# prev = 3
# curr = 4
# next = 5
# curr.next = 3
# prev = 4
# curr = 5

# step-3:
# prev = 2
# curr = 3
# next = 4
# curr.next = 2
# prev = 3
# curr = 4

# step - 1:
#     prev = None
#     curr = 1
#     next = 2
#     curr.next = None
#     prev = 1
#     curr = 2

# step-2:
# prev = 1
# curr = 2
# next = 3
# curr.next = 1
# prev = 2
# curr = 3
# # 1 2 3 4 5 6

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)
print("Given linked list:")
llist.printList()
llist.reverse()
print("\n L-List after reverse:")
llist.printList()
print("\n")