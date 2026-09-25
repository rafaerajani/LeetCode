class Solution(object):
    def removeElement(self, nums, val):
        # loop through the array
        # keep track of a read and a write
        # write == k
        # if read finds an element that is != val, write that into the write index, update write to write+=1
        # return write
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k

        # Notes: This is a simple two pointer solution, one pointer reads, the other writes, when we find a match, we write into the write position, and then iterate, this allows us to overwrite the elements == val by "shifting the entire array down"

        # Time Complexity = O(n)
        # Space Complexity = O(1)