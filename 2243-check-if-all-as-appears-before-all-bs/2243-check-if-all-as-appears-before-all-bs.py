class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)):
            if s[i] < s[i - 1]:
                return False
        return True