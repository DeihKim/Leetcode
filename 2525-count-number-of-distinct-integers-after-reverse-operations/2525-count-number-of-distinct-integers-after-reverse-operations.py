class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        rev = []
        for num in nums:
            rev.append(int(str(num)[::-1]))
        return len(nums | set(rev)) # | returns the union of nums and set(rev)