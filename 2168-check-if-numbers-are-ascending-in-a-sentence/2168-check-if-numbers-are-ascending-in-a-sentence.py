class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l1 = s.split()
        l2 = [int(token) for token in l1 if token.isdigit()]
        
        for i in range(len(l2) - 1):
            if l2[i] >= l2[i + 1]:
                return False
        
        return True
        
        '''
        Original
        last = -1
        tokens = s.split()
        for token in tokens:
            if token.isdigit():
                num = int(token)
                if num <= last:
                    return False
                last = num
        return True
        '''