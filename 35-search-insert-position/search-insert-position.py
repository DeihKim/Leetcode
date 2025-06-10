class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lIndex = len(nums)
        if nums[0] > target:
            return 0
            
        for i in range(lIndex):
            if nums[i] == target:
                return i
            elif i < lIndex - 1:
                if target > nums[i] and target < nums[i + 1]:
                    return i + 1
        return i + 1