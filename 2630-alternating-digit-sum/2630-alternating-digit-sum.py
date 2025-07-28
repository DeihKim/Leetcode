class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sign = 1
        ans = 0
        for num in str(n):
            ans += int(num) * sign
            sign *= -1
        return ans