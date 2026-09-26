class Solution(object):
    def majorityElement(self, nums):
        # keep a running count of the current highest element
        # start with element 0, with count of 1, then when count equal 0 switch to next element
        majority = nums[0]
        count = 1
        for num in nums:
            if num == majority:
                count += 1
            else: 
                count -= 1

            if count == 0:
                majority = num
                count = 1
        return majority
        # Note: this approach is called the Boyer-Moore Voting algorithm where we keep a running count
        # the approach works because in layman terms, the majority will always cut out any other front runner
        
        # Time Complexity = O(n)
        # Space Complexity = O(1)
