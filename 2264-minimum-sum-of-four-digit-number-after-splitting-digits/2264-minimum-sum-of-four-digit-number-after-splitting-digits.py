class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = sorted(str(num))
        return int(num[0]) * 10 + int(num[2]) + int(num[1]) * 10 + int(num[3])