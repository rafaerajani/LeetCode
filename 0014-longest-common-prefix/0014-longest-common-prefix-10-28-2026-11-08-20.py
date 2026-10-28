class Solution(object):
    def longestCommonPrefix(self, strs):
        # take the first string
        # (longest common prefix can only be as long as the length of the shortest string)
        # for each character in string 1 (enumerate)
        # for each string in strs
        # if string[i] = character then continue
        # if i is out of boundsthen that means i-1 is the max length
        # so we check i out of bounds first

        reference = strs[0]
        for i, character in enumerate(reference):
            for string in strs:
                if (i + 1) > len(string) or character != string[i]:
                    return reference[:i]

        return reference

