class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        bit = 0
        for char in binary:
            if char == '1':
                bit += 1
        return bit
        '''
        bit = 0
        while n > 0:
            n &= (n - 1)
            bit += 1
        return bit
        '''