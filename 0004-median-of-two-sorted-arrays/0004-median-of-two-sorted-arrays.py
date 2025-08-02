class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        length = len(nums)
        mid = length / 2
        if length % 2 == 0:
            return (nums[mid] + nums[mid - 1]) / 2.0
        return nums[mid]