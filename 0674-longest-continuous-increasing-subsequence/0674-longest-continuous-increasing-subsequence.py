class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        maxSeq = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count +=1
            else:
                count = 1
            
            if count > maxSeq:
                maxSeq = count
        return maxSeq