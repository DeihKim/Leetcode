class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxDigitV = defaultdict(int)
        maxSum = -1
        for num in nums:
            maxD = max(str(num))

            if maxD in maxDigitV:
                maxSum = max(maxSum, maxDigitV[maxD] + num)
            
            maxDigitV[maxD] = max(maxDigitV[maxD], num)
        return maxSum