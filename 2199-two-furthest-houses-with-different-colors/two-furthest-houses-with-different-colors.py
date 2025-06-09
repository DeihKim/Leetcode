class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """

        l = 0
        r = len(colors) - 1
        dist = 0

        while r > l:
            if colors[r] != colors[l]:
                dist = r - l
                break
            r -= 1
        
        l = 0
        r = len(colors) - 1

        while l < r:
            if colors[l] != colors[r]:
                dist = max(dist, r - l)
                break
            l += 1
        
        return dist
        