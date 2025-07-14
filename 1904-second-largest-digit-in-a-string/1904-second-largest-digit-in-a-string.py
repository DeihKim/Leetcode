class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit = set()
        for c in s:
            if c >= '0' and c <= '9':
                digit.add(int(c))
        digit = sorted(list(digit))
        return digit[len(digit) - 2] if len(digit) > 1 else -1