class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        for i in range(3, n + 1):
            if i % 3 == 0:
                total += i
            elif i % 5 == 0:
                total += i
            elif i % 7 == 0:
                total += i
        return total