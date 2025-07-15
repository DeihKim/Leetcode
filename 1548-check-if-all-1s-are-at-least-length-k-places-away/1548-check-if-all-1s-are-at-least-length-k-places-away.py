class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last = None
        for i, num in enumerate(nums):
            if num == 1:
                if last is not None and i - last - 1 < k:
                    return False
                last = i
        return True
