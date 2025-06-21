class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sumRange = n * (n + 1) / 2
        return sumRange - sum(nums)

        '''
        Original
        nums.sort()
        hset = []
        for i in range(len(nums) + 1):
            hset.append(i)
        
        for i in range(len(hset)):
            if hset[i] not in nums:
                return hset[i]
        '''