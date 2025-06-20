class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        curr = nums[0]
        majelemnt = 1

        for i in range(1, len(nums)):
            if nums[i] == curr:
                majelemnt += 1
            elif majelemnt > len(nums)/2:
                return curr
            else:
                curr = nums[i]
                majelemnt = 1
        
        return curr