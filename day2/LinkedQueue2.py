from DoublyLikedList import DoublyLinkedList

class ComposedLinkedQueue: # 1. Composition
    def __init__(self):
        self.dll = DoublyLinkedList() # Composition

    def put(self, value):
        return self.dll.append(value)

    def get(self):
        value = self.dll.access(0)
        if value is not None:
            self.dll.remove(0)
        return value

    def peek(self):
        return self.dll.access(0)

    def print(self):
        self.dll.print()


class DerivedLinkedQueue(DoublyLinkedList): # 상속에 의한 구현 (Inheritance)
    def __init__(self):
        super().__init__()

    def put(self, value):
        return self.append(value)

    def get(self):
        value = self.access(0)
        if value is not None:
            self.remove(0)
        return value
    
    def peek(self):
        return self.access(0)

    def print(self):
        super().print()

        
if __name__=="__main__":
    composedLinkedQueue = ComposedLinkedQueue()
    composedLinkedQueue.put(5)
    composedLinkedQueue.print()