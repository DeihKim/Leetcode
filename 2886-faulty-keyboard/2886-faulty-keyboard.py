class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            if s[i] != 'i':
                res += s[i]
            else:
                res = res[::-1]
        return res