class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i - 1]
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                count += 1
            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                count += 1
        return count