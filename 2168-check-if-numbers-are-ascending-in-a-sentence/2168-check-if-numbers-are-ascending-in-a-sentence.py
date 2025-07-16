class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        last = -1
        tokens = s.split()
        for token in tokens:
            if token.isdigit():
                num = int(token)
                if num <= last:
                    return False
                last = num
        return True