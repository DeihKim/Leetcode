class Solution(object):
    from collections import Counter
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums).most_common()
        freq.sort(key = lambda x: x[0], reverse = True)
        freq.sort(key = lambda x: x[1])
        
        res = []
        for num in freq:
            n, f = num
            res.extend([n] * f)

        return res