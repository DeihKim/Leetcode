class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxNum = max(nums)
        minNum = min(nums)

        if maxNum - minNum - 2*k <= 0:
            return 0
        return maxNum - minNum - 2*k