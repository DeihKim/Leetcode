class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        n = len(arr)        
        arr.sort()

        list = []
        minDiff = abs(arr[1] - arr[0])

        for i in range(n - 1):
            minDiff = min(minDiff, abs(arr[i + 1] - arr[i]))

        for i in range(n - 1):
            if abs(arr[i + 1] - arr[i]) == minDiff:
                list.append([arr[i], arr[i + 1]])
        
        return list
        