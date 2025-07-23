class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def increasing(nums):
            res = -float('inf')
            for n in nums:
                if n < res:
                    return False
                res = n
            return True
        
        def decreasing(nums):
            res = float('inf')
            for n in nums:
                if n > res:
                    return False
                res = n
            return True
        
        return increasing(nums) or decreasing(nums)
        
        '''
        increasing = True
        decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            elif nums[i] < nums[i + 1]:
                decreasing = False
            if not increasing and not decreasing:
                break
        return increasing or decreasing
        '''