class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedNums = sorted(nums)
        seen = {}
        count = 0
        for num in sortedNums:
            if num not in seen:
                seen[num] = count
            count += 1

        res = []
        for num in nums:
            res.append(seen[num])
        return res