import array

class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)
    
    def is_empty(self):
        return self.length == 0
    
    def get_capacity(self):
        self.capacity *= 2
        new_arr = array.array('l', [0]*self.capacity)
        for i in range(self.length):
            new_arr[i] = self.array[i]
        self.array = new_arr
    
    def check_index(self, index):
        if index >= self.length or index < 0:
            print('Index Error')
            return
    
    def prepend(self, value):
        if self.length == self.capacity:
            self.get_capacity()
            
        for i in range(self.length - 1, -1, -1):
            self.array[i + 1] = self.array[i]
        
        self.array[0] = value
        self.length += 1
                
    def append(self, value):
        if self.length == self.capacity:
            self.get_capacity()
            
        self.array[self.length] = value
        self.length += 1

    def set_head(self, index):
        self.check_index(index)
        self.array = self.array[index:]
        self.capacity -= index
        self.length -= index

    def access(self, index):
        self.check_index(index)
        return self.array[index]

    def insert(self, index, value):
        self.check_index(index)
        if self.length == self.capacity:
            self.get_capacity()
            
        for i in range(self.length - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        
        self.array[index] = value
        self.length += 1

    def remove(self, index):
        self.check_index(index)
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1

    def print(self):
        if self.is_empty():
            print('ArrayList is empty.')
        else:
            print('ArrayList =>', end=' ')
            for i in self.array.tolist()[:self.length]:
                print(i, end=' ')
            print()
        

array_list = ArrayList(5)
array_list.print()

for i in range(7):
    array_list.prepend(i + 1)
array_list.print()

for i in range(7):
    array_list.append(i + 10)
array_list.print()

array_list.set_head(5)
array_list.print()

array_list.insert(5,1000)
array_list.print()

array_list.remove(3)
array_list.print()

print(array_list.access(4))