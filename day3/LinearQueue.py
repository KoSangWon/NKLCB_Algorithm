# Linear Queue
import array

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            return False

        self.array[self.rear] = value
        self.rear += 1
        return True

    def get(self):
        if self.front == self.rear:
            return None

        value = self.array[self.front]
        self.front += 1
        return value

    def peek(self):
        if self.front == self.rear:
            return None
        else:
            return self.array[self.front]

    def print(self):
        if self.front == self.rear:
            print('empty')
        else:
            for i in range(self.front, self.rear):
                print(self.array[i], end=' ')
            print()
                

linearQueue = LinearQueue(5)
for i in range(8):
    linearQueue.put(i + 1)
    linearQueue.print()

print(linearQueue.get())
print(linearQueue.get())

linearQueue.print()
print(linearQueue.peek())    