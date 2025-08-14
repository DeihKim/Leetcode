class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1

        for _ in range(n - 1):
            temp = one
            one = temp + two
            two = temp
        
        return one