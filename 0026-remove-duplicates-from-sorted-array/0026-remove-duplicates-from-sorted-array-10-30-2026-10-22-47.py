class Solution(object):
    def removeDuplicates(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: int
        # """
        # loop through nums as read
        # when nums read != nums write
        # then move write up one, rewrite it with read, continue.
        write = 0
        for num in nums:
            if num != nums[write]:
                write += 1
                nums[write] = num
        return write + 1
        
        # time complexity = O(n)
        # space complexity = O(1)