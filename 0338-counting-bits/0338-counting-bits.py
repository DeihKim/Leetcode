class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n + 1):
            res.append(str(bin(i)).count('1'))
        
        return res
        
        '''
        counter = [0]
        for i in range(1, n + 1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
        '''
            