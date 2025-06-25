class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = None
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if first == None or num > first:
                third = second
                second = first
                first = num
            elif second == None or num > second:
                third = second
                second = num
            elif third == None or num > third:
                third = num
        if third == None:
            return first
        return third