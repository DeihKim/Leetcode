class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        res = []
        carry = 1
        while i >= 0 or carry:
            if i >= 0:
                carry += digits[i]
                i -= 1
            res.append(carry % 10)
            carry //= 10
        return res[::-1]