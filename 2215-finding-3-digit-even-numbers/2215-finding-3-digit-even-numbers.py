class Solution(object):
    from collections import Counter
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        freq = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            integer = [num // 100, (num % 100) // 10, num % 10]
            intFreq = Counter(integer)
            if all(freq[n] >= intFreq[n] for n in integer):
                res.append(num)
        return res