class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        num_Zero = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + num_Zero < n:
                arr[i + num_Zero] = arr[i]
            if arr[i] == 0:
                num_Zero -= 1
                if i + num_Zero < n:
                    arr[i + num_Zero] = 0
            