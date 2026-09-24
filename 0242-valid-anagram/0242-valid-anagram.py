class Solution(object):
    def isAnagram(self, s, t):
        s_dict = {}
        for character in s:
            if character not in s_dict:
                s_dict[character] = 1
            else:
                s_dict[character] += 1
        for character in t:
            if character not in s_dict:
                return False
            else:
                s_dict[character] -= 1
        for key in s_dict:
            if s_dict[key] != 0:
                return False
        return True
        
        
        # s = "".join(sorted(s))
        # t = "".join(sorted(t))
        # return s == t

        # Notes: the commented solution is smaller, more compact but takes O(nlogn) time which is slower than this solution O(n) (simplified from O(3n)) this is mainly due to the use of sorted funciton in python

        # Time Complexity = O(n)
        # Space Complexity = O(1) as the size of the dict is not dependent on the length of the string, this is as duplicate characters can exist
        