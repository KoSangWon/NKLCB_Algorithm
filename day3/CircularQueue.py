# Circular Queue
import array

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.is_full = False
        self.array = array.array('l', [0]*capacity)

    def is_empty(self):
        return self.is_full is False
        
    def put(self, value):
        if self.is_full is True:
            return False # Overflow 발생
        
        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        
        if self.rear == self.front:
            self.is_full = True
            
        return True

    def get(self):
        if self.rear == self.front and self.is_empty():
            return False # Underflow 발생
        
        value = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.is_full = False
        return value

    def peek(self):
        if self.front == self.rear and self.is_empty():
            return None  # Underflow 발생
        return self.array[self.front]

    def print(self):
        s = ''
        startIdx = self.front
        endIdx = self.rear
        
        if self.rear == self.front and self.is_empty():
            print('[]')
            return 
    
        if endIdx <= startIdx:
            endIdx += self.capacity
        
        for i in range(startIdx, endIdx):
            s += str(self.array[i % self.capacity]) + ' '
        print(s)
        
                
circularQueue = CircularQueue(5)
for i in range(8):
    circularQueue.put(i + 1)
    circularQueue.print()

print(circularQueue.get())
print(circularQueue.get())

circularQueue.print()
print(circularQueue.peek())