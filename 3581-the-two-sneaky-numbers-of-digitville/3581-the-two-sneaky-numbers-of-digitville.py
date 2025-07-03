class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [0] * len(nums)
        res = []
        for num in nums:
            if arr[num] > 0:
                res.append(num)
            else:
                arr[num] = 1
        return res