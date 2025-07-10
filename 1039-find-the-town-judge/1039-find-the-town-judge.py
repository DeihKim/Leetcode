class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trusts = [0] * (n + 1)

        for i in range(len(trust)):
            trusts[trust[i][0]] -= 1
            trusts[trust[i][1]] += 1

        for i in range(1, len(trusts)):
            trustNum = trusts[i]
            if trustNum == n - 1:
                return i

        return -1