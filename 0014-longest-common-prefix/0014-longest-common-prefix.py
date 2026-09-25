class Solution(object):
    def longestCommonPrefix(self, strs):
        #loop through each character of the first word
        #then loop through each word at the index of that character
        # if mismatch cut it and return
        #otherwise iterate
        #if we finish the original word the nreturn the original word
        # test [a, ab]
        reference = strs[0]

        for i, character in enumerate(reference):
            for word in strs:
                if len(word) <= i or word[i] != character:
                    return reference[:i]

        return reference

        #Note: dont forget to check edge cases, such as if index is out of range for 
        # word, we needed that as part of the if statement.
        # Additionally if i > len(word) is already out of index, the correct one would
        # be if i == or > len of word as we would then get the proper edge case as 
        # index is 0 indexed, length is not
        
        # Time Complexity = O(n) (n being the length of strs[1])
        # Space Complexity = O(1)