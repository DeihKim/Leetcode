class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxRight = -1
        for i in range (len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = maxRight
            maxRight = max(maxRight, current)
        
        return arr