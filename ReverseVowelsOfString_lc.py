"""Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once."""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = "aeiouAEIOU"
        s = list(s)
        l = 0
        r = len(s)-1
        
        while l<r:
            if s[l] not in vow:
                l+=1
                continue
            if s[r] not in vow:
                r-=1
                continue
            
            s[l],s[r] = s[r],s[l]
            l +=1
            r -=1

        return "".join(s)
