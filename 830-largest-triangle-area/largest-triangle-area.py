class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        
        maxArea = 0
        length = len(points)
        for i in range(length):
            x1, y1 = points[i]
            for j in range(i + 1, length):
                x2, y2 = points[j]
                for k in range(j + 1, length):
                    x3, y3 = points[k]
                    area = abs(0.5 * (x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3))
                    if area > maxArea:
                        maxArea = area
        
        return maxArea

