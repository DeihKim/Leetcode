class Solution(object):
    from collections import Counter
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        res = set(nums[0])
        for i in range(1, len(nums)):
            res &= set(nums[i])
        res = list(res)
        res.sort()
        return res
        '''
        Original
        res = []
        arr = len(nums)
        nums = Counter(sum(nums, []))
        for num in nums:
            if nums[num] == arr:
                res.append(num)
        return sorted(res)
        '''