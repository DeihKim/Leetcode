class Solution(object):
    from collections import Counter
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = Counter(nums)
        for f in freq.values():
            if f > 2:
                return False
        return True