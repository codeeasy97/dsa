# Detect loop in linked list

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

    def makeLoop(self, pos):
        temp = self.head
        count = 1
        while count < pos:
            temp = temp.next
            count = count + 1
        backup = temp
        print("============",backup.data)
        while temp.next:
            temp = temp.next
        temp.next = backup

    def detectLoop(self):
        slow = fast = self.head
        while fast.next:
            if fast.next.next is not None:
                if fast.next.next.data == slow.next.data:
                    print(fast.next.next.data, slow.next.data)
                    return True
                fast = fast.next.next
                slow = slow.next
        return False

    def detectLoop2(self):
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

llist.makeLoop(3)

if llist.detectLoop():
    print("loop found")
else:
    print("loop not found")
