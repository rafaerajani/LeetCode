class MyHashSet(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        bucket = key % self.size

        for element in self.buckets[bucket]:
            if element == key:
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


# Notes:
# - Two different keys can land in the same bucket (a collision), e.g.
#   5 % 1000 == 1005 % 1000 == 5. Each bucket is a list so it can hold
#   several keys. This approach is called "chaining".
# - Bucket order is meaningless, which is why .remove() is fine here and we
#   don't need swap-and-pop.
# - The real speedup comes from jumping straight to one bucket (O(1) index)
#   instead of scanning everything.

# Time Complexity (add / remove / contains):
#   Average: O(1) when keys spread evenly, so each bucket stays tiny.
#   Worst:   O(n) if every key lands in the same bucket (e.g. all multiples
#            of 1000), because that bucket becomes one long list to scan.
# Space Complexity: O(n) for n stored keys. The 1000 empty buckets are a
#   fixed constant, so they don't change the Big-O.