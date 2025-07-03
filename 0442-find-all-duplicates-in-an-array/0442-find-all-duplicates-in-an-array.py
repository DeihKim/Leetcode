class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        Nlist = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                Nlist.append(num)
            nums[num - 1] *= -1
        return Nlist