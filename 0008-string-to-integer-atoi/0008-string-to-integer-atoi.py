class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxInt = 2**31 - 1
        minInt = -2**31

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:
            return 0
        
        sign = 1
        if i < n and s[i] == '+':
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1
        
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if res > (maxInt - digit) // 10:
                return maxInt if sign == 1 else minInt
            res = res * 10 + digit
            i += 1

        return sign * res

        '''
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
        '''