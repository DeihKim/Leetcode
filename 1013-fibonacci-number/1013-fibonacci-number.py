class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(n):
            if n <= 1:
                return n
            
            return f(n - 2) + f(n - 1)
        return f(n)