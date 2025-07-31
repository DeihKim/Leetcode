class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = bisect.bisect_left(nums, 0)
        pos = len(nums) - bisect.bisect_right(nums, 0)
        return max(pos, neg)

        '''
        pos = 0
        neg = 0
        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        
        return pos if pos >= neg else neg
        '''