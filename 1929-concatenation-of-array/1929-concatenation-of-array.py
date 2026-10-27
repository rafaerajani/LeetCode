class Solution(object):
    def getConcatenation(self, nums):
        ans = [0]*(2*len(nums))
        # enumerate so that you can get both the number and the index in one go
        for i, num in enumerate(nums):
            ans[i] = num
            ans[len(nums) + i] = num
        return ans

        # Time complexity = O(n)
        # space complexity is O(2n) which simplifies to O(n)
