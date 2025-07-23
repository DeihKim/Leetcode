class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evenIv = []
        oddIv = []
        for i in range(len(nums)):
            if i % 2 == 0:
                evenIv.append(nums[i])
            else:
                oddIv.append(nums[i])
        evenIv.sort()
        oddIv.sort(reverse = True)

        evenIndex = 0
        oddIndex = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evenIv[evenIndex]
                evenIndex += 1
            else:
                nums[i] = oddIv[oddIndex]
                oddIndex += 1
        return nums

