class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        for i in range(len(s)):
            s[i] = "".join(reversed(s[i]))
        return " ".join(s)