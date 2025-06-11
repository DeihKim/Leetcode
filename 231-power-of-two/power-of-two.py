class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        """
        Any power of two has exactly one bit set in its binary representation.
        E.g, 8  is 1000 and 16 is 10000.
        If you subtract 1 from such numbers, all bits to the right of the set bit become 1,
        and a bitwise AND (&) will result in zero.
        8 =     1000
        8 - 1 = 0111
        8 & 7 = 0000
        """

        return n > 0 and n & (n - 1) == 0 
        