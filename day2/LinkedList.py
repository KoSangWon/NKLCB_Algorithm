class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def prepend(self, value):
        if self.head:
            node = Node(value, self.head)
        else:
            node = Node(value, None)
        self.head = node

    def append(self, value):
        if self.head:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = Node(value, None)
        else:
            self.head = Node(value, None)  
            
    def set_head(self, index):
        if self.head:
            cur_node = self.head
            for _ in range(index):
                cur_node = cur_node.next
            self.head = cur_node
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
        cur_node.next = Node(value, cur_node.next)

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        
        cur_node = self.head
        for _ in range(index - 1):
            cur_node = cur_node.next
        next_node = cur_node.next.next
        cur_node.next = next_node
            
    def print(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.value, end=' ')
            cur_node = cur_node.next
        print()
        
singlyLinkedList = SinglyLinkedList()

for i in range(7):
    singlyLinkedList.prepend(i + 1)
singlyLinkedList.print()

for i in range(7):
    singlyLinkedList.append(i + 10)
singlyLinkedList.print()

singlyLinkedList.set_head(5)
singlyLinkedList.print()

singlyLinkedList.insert(5,1000)
singlyLinkedList.print()

singlyLinkedList.remove(3)
singlyLinkedList.print()

print(singlyLinkedList.access(4))