class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [i, seen[target - num]]
            else:
                seen[num] = i
        return -1

        # Time complexity = O(n)
        # space complexity = O(n-1) = O(n)

        