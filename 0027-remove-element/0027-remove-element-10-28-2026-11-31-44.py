class Solution(object):
    def removeElement(self, nums, val):
        # two directional pointers
        # write goes left to right
        # read goes left to right
        # write only progress once written into
        # read will let write write only if its != val

        write = 0
        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
        return write

        # Time complexity = O(n)
        # Space Complexity = O(1)