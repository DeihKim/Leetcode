class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minVal = min(nums)
        maxVal = max(nums)
        
        for i in range(len(nums)):
            if nums[i] != minVal and nums[i] != maxVal:
                return nums[i]
        
        return -1