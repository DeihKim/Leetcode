class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        eSum = 0
        dSum = 0
        for num in nums:
            eSum += num
            dSum += sum(map(int, str(num)))
        return abs(eSum - dSum)