class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        indicesList = defaultdict(list)
        for i, num in enumerate(nums):
            indicesList[num].append(i)
        
        count = 0
        for indices in indicesList.values():
            for i in range(len(indices) - 1):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count