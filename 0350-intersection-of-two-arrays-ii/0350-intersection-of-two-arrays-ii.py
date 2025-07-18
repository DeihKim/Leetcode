class Solution(object):
    from collections import Counter

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = Counter(nums1)
        res = []
        for num in nums2:
            if nums1[num] > 0:
                res.append(num)
                nums1[num] -= 1
        return res
        '''
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        res = []
        for num, fq in nums1.items():
            res.append([num] * min(fq, nums2[num]))
        return sum(res, [])
        '''