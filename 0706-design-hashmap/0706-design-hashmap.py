class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key, value):
        bucket = key % self.size
        for i, pair in enumerate(self.buckets[bucket]):
            if pair[0] == key:
                self.buckets[bucket][i] = (key, value)
                return
        self.buckets[bucket].append((key, value))

    def get(self, key):
        bucket = key % self.size
        for pair in self.buckets[bucket]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        bucket = key % self.size
        for i, pair in enumerate(self.buckets[bucket]):
            if pair[0] == key:
                self.buckets[bucket].pop(i)
                return


# Notes:
# - Same structure as MyHashSet, except each bucket holds (key, value) tuples
#   instead of bare keys.
# - Each bucket must be a list ([]), not a tuple (()). The tuples live INSIDE
#   the list. Writing () for the buckets causes the .append() AttributeError.
# - put() scans the bucket once: overwrite in place if the key exists,
#   otherwise append after the loop finishes.
# - get() returns -1 when the key is missing (per the LeetCode spec).
# - remove() can't use list.remove(key) like MyHashSet, because the stored
#   items are (key, value) tuples and we don't know the value in advance.
#   Scanning with enumerate gives the index, so we pop it in the same pass.
#   A missing key just falls through the loop and does nothing.
# - In get() and remove(), only remove() needs enumerate; get() just needs pair.

# Time Complexity (put / get / remove):
#   Average: O(1) when keys spread evenly across buckets.
#   Worst:   O(n) if every key lands in the same bucket, since that bucket
#            becomes one long list to scan.
# Space Complexity: O(n) for n stored key-value pairs. The 1000 empty
#   buckets are a fixed constant and don't change the Big-O.