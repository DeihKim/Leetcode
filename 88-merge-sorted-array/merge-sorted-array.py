class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return
        
        endIndex = len(nums1) - 1

        while n > 0 and m > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[endIndex] = nums1[m - 1]
                m -= 1
            else:
                nums1[endIndex] = nums2[n - 1]
                n -= 1
            endIndex -= 1
        
        while n > 0:
            nums1[endIndex] = nums2[n - 1]
            n -= 1
            endIndex -= 1