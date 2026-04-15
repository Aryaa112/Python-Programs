"""For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2."""

class Solution(object):
    def gcd(self,a,b):
        if b ==0:
            return a
        return self.gcd(b,a%b)

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        
        length = self.gcd(len(str1),len(str2))
        
        return str1[:length]
