# Chaining
class HashTable:
    def __init__(self, hash_func=None, bucket_size=16):
        if hash_func is None:
            self.hash_func = hash
        else:
            self.hash_func = hash_func

        self.bucket_size = bucket_size
        self.bucket = [None] * bucket_size
        
    def set(self, key, value):
        hash_value = self.hash_func(key)
        bucket_index = hash_value % self.bucket_size

        node = self.bucket[bucket_index]
        if node is None:
            self.bucket[bucket_index] = [key, value, None]
            return
        
        prev = None
        while node:
            if node[0] == key:
                node[1] = value
                return

            prev = node
            node = node[2]
        
        prev[2] = [key, value, None]

    def get(self, key):
        hash_value = self.hash_func(key)
        bucket_index = hash_value % self.bucket_size

        node = self.bucket[bucket_index]
        while node:
            if node[0] == key:
                return node[1]
            node = node[2]
        return None

    def delete(self, key):
        hash_value = self.hash_func(key)
        bucket_index = hash_value % self.bucket_size

        node = self.bucket[bucket_index]
        # if node is None:
        #     return
        prev = None
        while node:
            if node[0] == key:
                if prev is not None:
                    prev[2] = node[2]
                    return
                else:
                    self.bucket[bucket_index] = node[2]
                    return
            prev = node
            node = node[2]
        return

    def print_hash(self):
        print(self.bucket)

# Open Addressing
class HashTable2:
    def __init__(self, hash_func=None, bucket_size=16):
        if hash_func is None:
            self.hash_func = hash
        else:
            self.hash_func = hash_func

        self.bucket_size = bucket_size
        self.bucket = [None] * bucket_size
        self.count = 0
        
    def insert(self, key, value):
        if self.count >= self.bucket_size:
            return
        hash_value = self.hash_func(key)
        bucket_index = hash_value % self.bucket_size
        # 없어도 되지만 가독성을 위해 추가
        node = self.bucket[bucket_index]
        if node is None:
            self.bucket[bucket_index] = [key, value]
            return

        for i in range(bucket_index, self.bucket_size):
            if self.bucket[i] is None:
                self.bucket[i] = [key, value]
                return
            elif self.bucket[i][0] == key:
                self.bucket[i][1] = value
                return

    def delete(self, key):
        pass

    def print_table(self):
        print(self.bucket)
     

ht = HashTable(hash_func=lambda x: x % 20)
ht.set(0, 'a')
ht.set(20, 'b')
ht.set(40, 'c')

print(ht.get(0))
print(ht.get(20))
print(ht.get(40))
print(ht.get(60))
ht.print_hash()
