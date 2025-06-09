class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        maxDiff = -1
        for i in range(1, len(nums)):
            if nums[i] < min:
                min = nums[i]
            elif nums[i] > min and nums[i] - min > maxDiff:
                maxDiff = nums[i] - min

        return maxDiff