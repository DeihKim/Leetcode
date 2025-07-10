class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        diff = (sum(aliceSizes) - sum(bobSizes)) /2
        for b in set(bobSizes):
            if b + diff in set(aliceSizes):
                return [b + diff, b]