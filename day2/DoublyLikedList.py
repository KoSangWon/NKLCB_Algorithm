class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None

    def prepend(self, value):
        if self.head:
            node = Node(value, self.head, None)
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = Node(value, None, None)

    def append(self, value):
        if self.head:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = Node(value, None, None)

    def set_head(self, index):
        if self.head:
            cur_node = self.head
            for _ in range(index):
                cur_node = cur_node.next
            self.head = cur_node
            self.head.prev = None
            return True
        else:
            return False

    def access(self, index):
        if self.head:
            cur_node = self.head
            for _ in range(index):
                cur_node = cur_node.next
            return cur_node.value
        else:
            return False

    def insert(self, index, value):
        if index == 0:
            self.append(value)
            return
        
        cur_node = self.head
        for _ in range(index - 1):
            cur_node = cur_node.next
        node = Node(value, cur_node.next, cur_node)
        cur_node.next.prev = node
        cur_node.next = node
        
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        cur_node = self.head
        for _ in range(index - 1):
            cur_node = cur_node.next
        next_node = cur_node.next.next
        cur_node.next = next_node
        next_node.prev = cur_node
        

    def print(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.value, end=' ')
            cur_node = cur_node.next
        print()
        
    def print_inverse(self):
        cur_node = self.tail
        while cur_node != None:
            print(cur_node.value, end=' ')
            cur_node = cur_node.prev
        print()
        
doublyLinkedList = DoublyLinkedList()

for i in range(7):
    doublyLinkedList.prepend(i + 1)
doublyLinkedList.print()
doublyLinkedList.print_inverse()

print()

for i in range(7):
    doublyLinkedList.append(i + 10)
doublyLinkedList.print()
doublyLinkedList.print_inverse()

print()

doublyLinkedList.set_head(5)
doublyLinkedList.print()
doublyLinkedList.print_inverse()

print()

doublyLinkedList.insert(5,1000)
doublyLinkedList.print()
doublyLinkedList.print_inverse()

print()

doublyLinkedList.remove(3)
doublyLinkedList.print()
doublyLinkedList.print_inverse()

print()

print(doublyLinkedList.access(4))