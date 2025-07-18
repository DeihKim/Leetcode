class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romInt[s[i]] < romInt[s[i + 1]]:
                res -= romInt[s[i]]
            else:
                res += romInt[s[i]]
        return res