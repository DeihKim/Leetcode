class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        seqSum = nums[0]
        for i in range(1, n):
            if nums[i] - nums[i - 1] != 1:
                break
            seqSum += nums[i]
        
        while seqSum in nums:
            seqSum += 1
        
        return seqSum