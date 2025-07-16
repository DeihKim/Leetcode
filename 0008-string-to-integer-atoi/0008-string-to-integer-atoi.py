class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        
        i = 0
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = 1 if s[i] == '+' else -1
            i += 1

        res = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if res > (2**31 - 1 - digit) // 10: # came from res*10 + digit > 2**31 - 1
                return 2**31 - 1 if sign == 1 else -2**31
            res = res * 10 + digit
            i += 1

        return sign * res