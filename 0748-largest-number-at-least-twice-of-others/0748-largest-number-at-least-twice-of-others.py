class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = 0
        prev = 0
        for i in range(len(nums)):
            if nums[i] > maxNum:
                prev = maxNum
                maxNum = nums[i]
                res = i
            elif nums[i] > prev:
                prev = nums[i]
        if maxNum >= prev * 2:
            return res
        return -1