class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # Pattern: Sliding Window (fixed size k), set as the window state
        # Time: O(n) - each element is added once and removed at most once
        # Space: O(min(n, k)) - the set never holds more than k elements

        seen = set()  # values currently in the window (the last k elements)

        for i, num in enumerate(nums):
            # Is this value already within the last k positions?
            # Set lookup is O(1) on average; a list would be O(k)
            if num in seen:
                return True

            seen.add(num)

            # Window now covers indices i-k..i. Once it holds more than k
            # elements (i + 1 > k, same as i >= k), drop the oldest one.
            # Safe from KeyError: the window has no duplicates, otherwise
            # we would have returned True above.
            if i + 1 > k:
                seen.remove(nums[i - k])

        return False  # no two equal values were within k indices

        # Brute force: for each i, compare with the next k elements -> O(n*k)
        # Alternative: dict of value -> last index, check i - last[num] <= k
        #   (O(n) time, O(n) space, no window needed)
        # Current solution
        # Time complexity = O(n)
        # Space Complexity = O(k)   
        