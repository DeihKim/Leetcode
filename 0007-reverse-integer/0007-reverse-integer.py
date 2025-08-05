class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1]) * sign
        return res if -2**31 <= res <= 2**31 - 1 else 0