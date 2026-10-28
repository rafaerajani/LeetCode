class Solution(object):
    def reverseString(self, s):
        # use a buffer system
        # left pointer
        # right pointer
        # buffer
        right = len(s) - 1
        for left, character in enumerate(s):
            if left > right:
                break
            else: 
                buffer = character
                s[left] = s[right]
                s[right] = buffer
                right -= 1

# time complexity = O(n/2) = O(n)
# space complexity = O(1)
