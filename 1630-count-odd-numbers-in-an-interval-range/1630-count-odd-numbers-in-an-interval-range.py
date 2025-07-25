class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low % 2 == 0:
            return (high - low + 1) // 2
        return (high - low) // 2 + 1