class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range(self.size)]

    def put(self, key, value):
        bucket = key % self.size

        for i, pair in enumerate(self.buckets[bucket]):
            if pair[0] == key:
                self.buckets[bucket][i] = (key, value)
                return
        self.buckets[bucket].append((key,value))
        

    def get(self, key):
        bucket = key % self.size
        for pair in self.buckets[bucket]:
            if pair[0] == key:
                return pair[1]
        return -1
        

    def remove(self, key):
        bucket = key % self.size
        for i, pair in enumerate(self.buckets[bucket]):
            if key == pair[0]:
                self.buckets[bucket].pop(i)
                return
        return
        

# time complexity = O(1) if evenly spread otherwise worst case is O(n)
# space complexity - O(n) as buckets are fixed.
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)