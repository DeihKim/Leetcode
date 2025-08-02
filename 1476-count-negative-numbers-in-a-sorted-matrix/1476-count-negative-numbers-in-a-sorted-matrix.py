class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        for arr in grid:
            neg = bisect.bisect_left(sorted(arr), 0)
            total += neg
        
        return total