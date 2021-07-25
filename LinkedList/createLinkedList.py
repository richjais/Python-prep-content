class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


linklist = LinkedList()
len = int(input())
linklist.head=Node(int(input()))
for _ in len-1:
    newnode = Node(int(input()))
    linklist.next = newnode