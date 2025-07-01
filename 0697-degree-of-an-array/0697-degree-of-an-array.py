class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        start = {}
        end = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
                start[nums[i]] = i
            end[nums[i]] = i
        maxCount = max(count.values())
        
        minLength = float('inf')
        for num in count:
            if count[num] == maxCount:
                length = end[num] - start[num] + 1
                minLength = min(length, minLength)
        return minLength