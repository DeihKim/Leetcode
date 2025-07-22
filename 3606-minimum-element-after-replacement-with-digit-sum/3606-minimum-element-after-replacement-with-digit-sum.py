class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        replaced = []
        for num in nums:
            replaced.append(sum(map(int, str(num))))
        return min(replaced)