class Solution(object):
    def isPalindrome(self, s):
        # first clean the string
        # then two pointers, left and right
        # if they ever dont equal, return false
        # else if the while loop completes, then return true


        cleaned = "".join(c.lower() for c in s if c.isalnum())

        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True

# Notes:
# - Clean the string first: keep only alphanumeric characters, lowercased.
#   join glues an iterable of strings together, with "" as the separator.
# - For each character, the filter (isalnum) and the lower() run together,
#   one character at a time. join assembles the results at the end.
# - Then two pointers, left and right, move towards each other (same as Reverse
#   String). If a pair ever differs, return False. If left and right meet or
#   cross, every pair matched, so return True.

# Time Complexity = O(n)
#   Cleaning pass over s: O(n). Two-pointer loop: O(n/2). O(n) + O(n/2) = O(n).
# Space Complexity = O(n)
#   cleaned is a new string of up to n characters (strings are immutable, so
#   it can't be edited in place). The two pointers are O(1), but cleaned dominates.
#   Skipping non-alphanumeric characters with the pointers directly gets O(1) space.

# NOTE: built in python functionality --> return cleaned == cleaned[::-1]
