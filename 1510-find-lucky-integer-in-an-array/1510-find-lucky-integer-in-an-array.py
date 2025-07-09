class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freqncy = {}
        for num in arr:
            if num in freqncy:
                freqncy[num] += 1
            else:
                freqncy[num] = 1
        
        lucky = []
        for num, fq in freqncy.items():
            if num == fq:
                lucky.append(num)
        
        return max(lucky) if lucky else -1