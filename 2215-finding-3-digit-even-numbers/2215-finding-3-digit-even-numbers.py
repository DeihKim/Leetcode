class Solution(object):
    from collections import Counter
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        freq = Counter(digits)
        res = []
        for i in range(1, 10):
            if freq[i] == 0: continue
            freq[i] -= 1
            for j in range(10):
                if freq[j] == 0: continue
                freq[j] -= 1
                for k in range(0, 10, 2):
                    if freq[k] == 0: continue
                    res.append(i * 100 + j * 10 + k)
                freq[j] += 1
            freq[i] += 1
        return res

        '''
        freq = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            integer = [num // 100, (num % 100) // 10, num % 10]
            intFreq = Counter(integer)
            if all(freq[n] >= intFreq[n] for n in intFreq):
                res.append(num)
        return res
        '''