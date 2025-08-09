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
        
        logNbase4 = math.log(n)/math.log(4)
        return logNbase4 == int(logNbase4)