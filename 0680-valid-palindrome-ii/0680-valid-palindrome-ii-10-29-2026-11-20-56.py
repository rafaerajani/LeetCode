class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                #two cases
                remLeft = s[:left] + s[left+1:]
                remRight = s[:right] + s[right + 1:]
                return remLeft == remLeft[::-1] or remRight == remRight[::-1]

            left += 1
            right -= 1
        return True

    # Notes:
    # - No cleaning needed: the problem guarantees lowercase letters only.
    # - Run the normal two-pointer palindrome check. At the first mismatch, we get
    #   one chance to remove a character, and we don't know which side it's on, so
    #   build two new strings: one without s[left], one without s[right].
    # - If either is a palindrome (equals its reverse), return True, otherwise False.
    # - Only one branch ever happens, because we return right after the first mismatch.

    # Time Complexity = O(n)
    #   Main scan O(n/2) + building and checking two new strings, each O(n).
    # Space Complexity = O(n)
    #   remLeft, remRight and a temporary reversed copy: a few strings of up to n
    #   characters each. The index-based helper approach avoids this and uses O(1).