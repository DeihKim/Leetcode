class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return 0

        left, right = 1, x
        res = 0

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return res
