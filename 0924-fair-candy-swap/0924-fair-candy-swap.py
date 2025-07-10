class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        aliceSizes = set(aliceSizes)

        for b in bobSizes:
            if b + diff in aliceSizes:
                return (b + diff, b)