class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 3 pointers

        # one write starting from right
        # one read going left for nums1 starting at m
        # one read going left starting from right of nums2

        # write pointer only moves after being written into
        # loop through nums 2

        write = m + n - 1        
        read1 = m - 1
        read2 = n - 1

        while read2 >= 0:
            if read1 < 0:
                nums1[write] = nums2[read2]
                read2 -= 1
            elif nums1[read1] > nums2[read2]:
                nums1[write] = nums1[read1]
                read1 -= 1
            else:
                nums1[write] = nums2[read2]
                read2 -= 1
            write -= 1
# Note, the else and if statement can be combined for a shorter solution
# time complexity = O(m+n)
# space complexity = O(1)