class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Nlist = {}
        for i in range(len(nums)):
            if nums[i] in Nlist:
                Nlist[nums[i]] += 1
            else:
                Nlist[nums[i]] = 1

        for v in Nlist:
            if Nlist[v] == 1:
                return v