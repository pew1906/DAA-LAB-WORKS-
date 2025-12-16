# Experiment 10: Hash Table for Student Records
import time
import random

def generate_students(n):
    students = []
    for i in range(n):
        student_id = 1000 + i
        name = f"Student_{i}"
        marks = random.randint(40, 100)
        students.append((student_id, name, marks))
    return students

class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break
        return None

def compare_access_times(num_students=10000):
    students = generate_students(num_students)
    
    ht_chain = HashTableChaining(size=20000)
    ht_linear = HashTableLinearProbing(size=20000)
    student_list = students.copy()

    for sid, name, marks in students:
        ht_chain.insert(sid, (name, marks))
        ht_linear.insert(sid, (name, marks))

    search_keys = random.sample([sid for sid, _, _ in students], 1000)

    start = time.time()
    for key in search_keys:
        for sid, name, marks in student_list:
            if sid == key:
                break
    list_time = time.time() - start

    start = time.time()
    for key in search_keys:
        ht_chain.search(key)
    chain_time = time.time() - start

    start = time.time()
    for key in search_keys:
        ht_linear.search(key)
    linear_time = time.time() - start

    print(f"List Search Time:           {list_time:.6f} sec")
    print(f"Hash Table (Chaining):      {chain_time:.6f} sec")
    print(f"Hash Table (Linear Probe):  {linear_time:.6f} sec")

if __name__ == "__main__":
    compare_access_times()
