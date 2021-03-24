# Stack
import array

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = array.array('l', [0]*capacity)
    
    def push(self, value):
        if self.top == self.capacity:
            return False
        else:
            self.array[self.top] = value
            self.top += 1
            return True

    def pop(self):
        if self.top == 0:
            return None
        else:
            self.top -= 1
            return self.array[self.top - 1]
    
    def peek(self):
        if self.top == 0:
            return None
        else:
            return self.array[self.top - 1]
    
    def is_empty(self):
        return self.top == 0
    
    def print(self):
        print(self.array.tolist()[:self.top])
    
stack = Stack(10)
stack.print()

for i in range(7):
    stack.push(i + 1)
stack.print()

for _ in range(3):
    stack.pop()
stack.print()

print(stack.peek())
print(stack.pop())
stack.print()
print(stack.peek())

print(stack.is_empty())

