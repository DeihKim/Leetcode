class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n <= 0:
            return False
        
        sqrtN = math.sqrt(n)
        log2sqrtN = math.log(sqrtN)/math.log(2)
        return log2sqrtN == int(log2sqrtN)
        '''
        or
        if n == 1:
            return True
        if n <= 0:
            return False
        
        logNbase4 = math.log(n)/math.log(4)
        return logNbase4 == int(logNbase4)
        '''