class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = len(num) - 1
        res = []
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1
            res.append(k % 10)
            k //= 10
        return res[::-1]

        '''
        Original
        num1 = ''
        for digit in num:
            num1 += str(digit)
        total = str(int(num1) + k)
        res = []
        for digit in total:
            res.append(int(digit))
        return res
        '''