class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        sum = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                sum += i
                if i * i != num:
                    sum += num // i
        return sum == num