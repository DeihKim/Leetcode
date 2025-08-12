class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        res = ''
        carry = 0
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                digit1 = ord(num1[i]) - ord('0')
                i -= 1
            else:
                digit1 = 0

            if j >= 0:
                digit2 = ord(num2[j]) - ord('0')
                j -= 1
            else:
                digit2 = 0

            carry += digit1 + digit2
            res += chr(carry % 10 + ord('0'))
            carry //= 10
        return res[::-1]

        '''
        i = len(num1) - 1
        j = len(num2) - 1
        res = ''
        carry = 0
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1
            res += str(carry % 10)
            carry //= 10
        return res[::-1]
        '''