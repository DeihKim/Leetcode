class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        singleDigit = 0
        doubleDigit = 0
        for num in nums:
            if len(str(num)) == 1:
                singleDigit += num
            else:
                doubleDigit += num
        return True if singleDigit != doubleDigit else False