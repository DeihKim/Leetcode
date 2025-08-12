class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        num1 = ''
        for digit in num:
            num1 += str(digit)
        total = str(int(num1) + k)
        res = []
        for digit in total:
            res.append(int(digit))
        return res