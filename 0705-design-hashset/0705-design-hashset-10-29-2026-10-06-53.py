class MyHashSet(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[]]*self.size

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
        


# time complexity = O(1) if evenly spread, worst case is O(n)
# space complexity = O(n) as the 1000 buckets are fixed.
