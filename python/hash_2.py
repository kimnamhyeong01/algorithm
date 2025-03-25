class HashTable:
    def __init__(self, length = 5):
        self.max_len = length 
        self.table = [[] for _ in range(self.max_len)] 
    
    def set(self, key, value):
        index = hash(key) % self.max_len 
        self.table[index].append((key, value)) 
    
    def get(self, key):
        index = hash(key) % self.max_len 
        value = self.table[index] 
        if not value:
            return None 
        for v in value:
            if v[0] == key:
                return v[1] 
        return None