class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1 or (len(nums) == 2 and nums[0] == nums[1]):
            return nums
        nums.sort(reverse = True)
        for i in range(1, len(nums)):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]