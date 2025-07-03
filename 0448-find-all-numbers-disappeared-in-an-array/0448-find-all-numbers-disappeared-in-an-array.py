class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Improvement
        Nlist = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in Nlist]

        '''
        Original
        for n in nums:
            i = abs(n) - 1
            nums[i] = -abs(nums[i])
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        '''