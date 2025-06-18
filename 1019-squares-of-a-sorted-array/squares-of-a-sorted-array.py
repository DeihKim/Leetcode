class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        for i in range(length):
            nums[i] = nums[i] * nums[i]
        '''
        time limit exceeded TT
        swap = True
        while swap == True:
            swap = False
            for j in range(len(nums) - 1):
                if nums[j + 1] < nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swap = True
        '''

        nums.sort()
        
        return nums