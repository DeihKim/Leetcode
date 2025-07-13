class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        common = list(set(nums1) & set(nums2))
        minNum = float('inf')
        if common:
            for num in common:
                minNum = min(num, minNum)
            return minNum
        return -1