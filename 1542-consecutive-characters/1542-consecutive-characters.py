class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        maxCount = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 1
        return maxCount
        