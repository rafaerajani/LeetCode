class Solution(object):
    def reverseString(self, s):
        # use a buffer system
        # left pointer
        # right pointer
        # buffer
        right = len(s) - 1
        left = 0
        while left < right:
            buffer = s[left]
            s[left] = s[right]
            s[right] = buffer
            right -= 1
            left += 1
# NOTE: this is a cleaner solution and the more standard solution than the for loop
# time complexity = O(n/2) = O(n)
# space complexity = O(1)
