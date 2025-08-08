class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if 0 <= num <= 9:
            return True
        return True if int(str(int(str(num)[::-1]))[::-1]) == num else False