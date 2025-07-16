class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for lastdigit in range(len(num) - 1, -1, -1):
            if int(num[lastdigit]) % 2 != 0:
                return num[:lastdigit + 1]
        return ""