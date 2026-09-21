class Solution(object):
    def getConcatenation(self, nums):
        ans = [0]*(2*len(nums))
        for i, num in enumerate(nums):
            ans[i] = num
            ans[len(nums) + i] = num
        return ans