class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) == k:
                    count += 1
        return count