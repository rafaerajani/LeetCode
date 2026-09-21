class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
    # Notes
    #     - the reason we didnt compare the length of nums to the set nums is because
    #       on average it will be slower since it takes O(n) to convert a list to a set
    #     - this solution has better average performance, and the same worst case
    #       performance
    
    # Time Complexity = O(n)
    # Space Complexity = O(n)
        
