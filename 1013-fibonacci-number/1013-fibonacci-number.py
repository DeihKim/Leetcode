class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b

        '''
        def f(n:)
            if n <= 1:
                return n            
            return f(n - 2) + f(n - 1)
        return f(n)
        '''