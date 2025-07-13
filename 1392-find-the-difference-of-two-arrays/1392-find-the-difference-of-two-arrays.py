class Solution(object):
    def distint(self, arr1, arr2):
        res = []
        for num in arr1:
            if num not in arr2:
                res.append(num)
        return res
        

    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer = [0] * 2
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        answer[0] = self.distint(nums1, nums2)
        answer[1] = self.distint(nums2, nums1)
        return answer
