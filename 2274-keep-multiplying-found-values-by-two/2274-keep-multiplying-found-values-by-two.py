class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums = set(nums)
        while original in nums:
            original *= 2
        return original
        
        '''
        Original
        nums.sort()
        for num in nums:
            if num == original:
                original *= 2
        return original
        '''