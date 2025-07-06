class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        '''
        if k == 1:
            return s

        n = len(s)
        s = list(s)
        
        if n < k:
            s[0:] = s[::-1]
        else:

            left = 0
            right = k
            game = True
            while game:
                if len(s[left:]) < k:
                    s[left:] = s[-1:(n-left+1) * -1:-1]
                    game = False
                else:
                    s[left:right] = s[(n-right+1) * -1:(n-left+1) * -1:-1]
                    left += 2 * k
                    right += left'''
        n = len(s)
        s = list(s)
        for i in range(0, n, 2 * k):
            s[i:i + k] = reversed(s[i: i + k])

        return "".join(s)
