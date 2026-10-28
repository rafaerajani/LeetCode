class MyHashSet(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range (self.size)]

    def add(self, key):
        bucket = key % self.size
        for element in self.buckets[bucket]:
            if key == element:
                return
        self.buckets[bucket].append(key)
        

    def remove(self, key):
        bucket = key % self.size
        try:
            self.buckets[bucket].remove(key)
        except ValueError:
            pass
        

    def contains(self, key):
        bucket = key % self.size
        return key in self.buckets[bucket]
        

# NOTE: multiplying the empty array at the start creates 1000 references not 1000 empty lists, so in the end the initial solution took O(n) time every time. To fix it, use the for loop to create actually empty lists.
# time complexity = O(1) if evenly spread, worst case is O(n)
# space complexity = O(n) as the 1000 buckets are fixed.
