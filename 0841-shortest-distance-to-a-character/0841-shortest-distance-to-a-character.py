class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        ans = [0] * n
        cIndex = -float('inf')
        for i in range(n):
            if s[i] == c:
                cIndex = i
            ans[i] = i - cIndex
        
        cIndex = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                cIndex = i
            ans[i] = min(ans[i], cIndex - i)
        return ans

        '''
        Original

        indices = []
        n = len(s)
        for i in range(n):
            if s[i] == c:
                indices.append(i)
        
        ans = [] * n
        i = 0
        while i < n:
            minDis = float('inf')
            for index in indices:
                minDis = min(minDis, abs(i - index))
            ans.append(minDis)
            i += 1
        return ans
        '''