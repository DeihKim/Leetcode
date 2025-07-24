class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for i in nums]
        evenIndex = 0
        oddIndex = 1
        for num in nums:
            if num % 2 == 0:
                res[evenIndex] = num
                evenIndex += 2
            else:
                res[oddIndex] = num
                oddIndex += 2
        return res
    
        '''
        Original
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
        '''