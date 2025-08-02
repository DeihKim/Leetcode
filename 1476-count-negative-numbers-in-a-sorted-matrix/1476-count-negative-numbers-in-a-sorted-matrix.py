class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        m, n = len(grid), len(grid[0])
        col, row = 0, m - 1
        
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += n - col
                row -= 1
            else:
                col += 1
        
        return count

        '''Origianl
        total = 0
        for arr in grid:
            neg = bisect.bisect_left(sorted(arr), 0)
            total += neg
        
        return total
        '''