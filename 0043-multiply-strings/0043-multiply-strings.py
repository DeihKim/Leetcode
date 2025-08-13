class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n, m = len(num1), len(num2)
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                multiply = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = multiply + res[i + j + 1]
                res[i + j + 1] = sum_ % 10
                res[i + j] += sum_ // 10
        
        product = ''.join(map(str, res)).lstrip('0')
        return product if product else '0'