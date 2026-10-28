class Solution(object):
    def majorityElement(self, nums):

        count = 1
        majority = nums[0]
        for num in nums:
            if num == majority:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                majority = num
                count += 1
        return majority

        # Boyer Moore voting algorithm
        # Time complexity = O(n)
        # Space complexit = O(1)