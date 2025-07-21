class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        fq = {}
        for ch in num:
            digit = int(ch)
            if digit in fq:
                fq[digit] += 1
            else:
                fq[digit] = 1
        
        for digit, ch in enumerate(num):
            freq = int(ch)
            if digit in fq and freq != fq[digit]:
                return False
            elif digit not in fq and freq != 0:
                return False
    
        return True