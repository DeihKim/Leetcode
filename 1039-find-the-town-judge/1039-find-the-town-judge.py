class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        pTj = [0] * (n + 1)
        for i in range(len(trust)):
            pTj[trust[i][0]] -= 1
            pTj[trust[i][1]] += 1
        for i in range(1, len(pTj)):
            trustNum = pTj[i]
            if trustNum == n - 1:
                return i
        return -1