class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], i]
            seen[num] = i
        return None

        # Notes: logic is simple, instead of returning the values, we need to return the index, so in each iteration, check if the missing number (target - num) is in the dictionary, if it is, retrieve its index and the current index i and return both, otherwise add the currrent num and index to the dictionary.

        # Time complexity = O(n)
        # Space complexity = O(n) because all numbers could be unique, unlike valid Anagram where there are only 26 characters, there are infinite numbers
         