class Solution(object):
    def isAnagram(self, s, t):
        seen = {}
        for character in s:
            if character in seen:
                seen[character] += 1
            else:
                seen[character] = 1
        for character in t:
            if character not in seen:
                return False
            else:
                seen[character] -= 1
        for key in seen:
            if seen[key] != 0:
                return False
        return True
        
        # Time Complexity = O(n+k)
        # space Compelxity = O(1)