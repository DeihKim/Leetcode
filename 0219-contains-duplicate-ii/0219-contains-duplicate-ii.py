class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hset = {}

        for i in range(len(nums)):
            if nums[i] in hset and abs(i - hset[nums[i]]) <= k:
                return True
            hset[nums[i]] = i
        
        return False