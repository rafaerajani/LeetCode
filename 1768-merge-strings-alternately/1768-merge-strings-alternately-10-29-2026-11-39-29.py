class Solution(object):
    def mergeAlternately(self, word1, word2):
        parts = []
        for i, character in enumerate(word1):
            parts.append(character)
            if i < len(word2):
                parts.append(word2[i])
        
        if len(word2) > len(word1):
            parts.append(word2[len(word1):])
        return "".join(parts)
        # Notes:
# - One shared index i walks word1. For each character of word1 we add it, then
#   add word2[i] if word2 still has an index i. If word1 is longer, the loop
#   already covers its leftover characters.
# - Why a list + "".join instead of merged += ...:
#   strings are immutable, so each += builds a new string and copies everything
#   so far (1 + 2 + ... + n copies, about n^2/2). A list append is O(1) amortised,
#   and join allocates the result once and copies each piece once.
#   CPython sometimes optimises += in place, but that isn't guaranteed.
# - Why the last if is not required:
#   word2[len(word1):] is an empty string when word2 is not longer, because
#   slicing past the end returns "" instead of raising an error. join of an
#   empty piece adds nothing. The if just skips a pointless append.

# With += instead of a list:
#   Time:  O(n + m) in practice because of CPython's in-place optimisation,
#          but O((n + m)^2) in the worst case when the optimisation doesn't apply.
#   Space: O(n + m), the same, since the old intermediate strings are discarded.
#   The space doesn't change. The only difference is the guaranteed time bound.
# #################ACTUAL RESULTS FOR CURRENT SOLUTION##############
# Time Complexity = O(n + m)   (n = len(word1), m = len(word2))
#   Each character is added exactly once, and join is one pass.
# Space Complexity = O(n + m)
#   parts and the output string each hold up to n + m characters, and 2(n + m)
#   simplifies to O(n + m).