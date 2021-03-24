# Linked Queue
class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
    

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def put(self, value):
        if self.head is None:
            self.head = self.tail = Node(value, None, None)
        else:
            cur = self.tail
            node = Node(value, cur, None)
            cur.next = node
            self.tail = node
            return True

    def get(self):
        if self.head is None:
            return None
        
        if self.head == self.tail:
            value = self.head
            self.tail = self.head = None
            return value
        
        value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return value
    
    def peek(self):
        return self.head.value

    def print(self):
        cur = self.head
        while cur.next is not None:
            print(cur.value, end=' ')
            cur = cur.next
        print()
        

linkedQueue = LinkedQueue()
for i in range(8):
    linkedQueue.put(i + 1)
    linkedQueue.print()

print(linkedQueue.get())
print(linkedQueue.get())

linkedQueue.print()
print(linkedQueue.peek())    