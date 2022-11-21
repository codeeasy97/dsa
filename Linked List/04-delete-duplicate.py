# Remove duplicate from a linked list.
#sorted linked list
#Unsorted linked list


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
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def deleteDupSorted(self):
        temp = self.head
        while temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next

    def deleteDupUnsorted(self):
        nlist = []
        prev = self.head
        curr = self.head.next
        nlist.append(prev.data)
        while curr:
            if curr.data in nlist:
                prev.next = curr.next
                curr = curr.next
            else:
                nlist.append(curr.data)
                curr = curr.next
                prev = prev.next



llist = LinkedList()
llist.push(6) #prev1
llist.push(2) #curr1, prev2
llist.push(2) #curr2 #deleted
llist.push(5) #curr3 #prev3
llist.push(4) #curr4, #prev
llist.push(2) #curr5, 


llist.printList()
print("\n")
# llist.deleteDupSorted()
# llist.printList()

llist.deleteDupUnsorted()
llist.printList()
