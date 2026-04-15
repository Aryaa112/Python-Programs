"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string. """

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        p1 = p2 = 0
        res = ""
        l1 = len(word1)
        l2 = len(word2)
        for i in range(0, max(l1,l2)):
            if p1 < l1:
                res = res + word1[p1]
                p1 += 1
            if p2 < l2:
                res = res + word2[p2]
                p2 += 1
        return res
