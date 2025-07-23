class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse = True)

        evenIndex = 0
        oddIndex = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even[evenIndex]
                evenIndex += 1
            else:
                nums[i] = odd[oddIndex]
                oddIndex += 1
        return nums

