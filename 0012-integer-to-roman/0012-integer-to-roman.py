class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        res = ''
        for i in range(len(integer)):
            if num == 0:
                break
            
            times = num // integer[i]
            res += roman[i] * times
            num = num % integer[i]
        
        return res