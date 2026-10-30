class Solution(object):
    def groupAnagrams(self, strs):
        # """
        # :type strs: List[str]
        # :rtype: List[List[str]]
        # """
        # # create a dictionary
        # # the key will be a sorted string
        # # the value will be an array of words from the original array
        # # loop through strs
        # # sort the string
        # # if sorted string in dictionary, then append
        # # otherwise add sorted string and append

        # # "".join(sorted(string))
        anagrams = {}

        for string in strs:
            sort = "".join(sorted(string))
            if sort not in anagrams:
                anagrams[sort] = []

            anagrams[sort].append(string)
        return list(anagrams.values())

        # Time Complexity = O(n * k log k)
        #   n = number of words, k = length of a word. Each word is sorted once
        #   (O(k log k)), and hashing the sorted string as a dict key costs O(k).
        #   The sort dominates, and it runs n times.
        # Space Complexity = O(n * k)
        #   Worst case (no two words are anagrams) the dict holds n new sorted
        #   strings of length k as keys. The word lists only reference strings that
        #   already exist in the input.