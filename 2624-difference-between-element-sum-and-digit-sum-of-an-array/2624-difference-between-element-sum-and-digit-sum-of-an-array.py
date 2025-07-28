class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        eSum = sum(nums)
        dSum = 0
        for num in nums:
            while num > 0:
                dSum += num % 10
                num //= 10
        return abs(eSum - dSum)
        
        '''
        Original
        eSum = 0
        dSum = 0
        for num in nums:
            eSum += num
            dSum += sum(map(int, str(num)))
        return abs(eSum - dSum)
        '''