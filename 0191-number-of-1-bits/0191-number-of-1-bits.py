class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit = 0
        while n > 0:
            n &= (n - 1)
            bit += 1
        return bit