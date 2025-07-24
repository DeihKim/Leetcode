class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        evenIndex = 0
        oddIndex = 0
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even[evenIndex])
                evenIndex += 1
            else:
                res.append(odd[oddIndex])
                oddIndex += 1
        return res