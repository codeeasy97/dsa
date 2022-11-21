# Remove loop in linked list

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

    def removeLoop(self):
        temp = self.head
        visited = []
        while temp:
            if temp in visited:
                temp.next = None
            visited.append(temp)
            temp = temp.next

    def detectLoop(self):
        temp = self.head
        visited = []
        while temp:
            if temp in visited:
                return True
            visited.append(temp)
            temp = temp.next
        return False

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)

llist.printList()

llist.head.next.next.next.next.next = llist.head

llist.removeLoop()
print("\n")
if llist.detectLoop():
    print("loop detected")
else:
    print("loop not found")

