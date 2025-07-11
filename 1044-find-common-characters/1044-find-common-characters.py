class Solution(object):
    def count(self, word):
        freqncy = [0] * 26
        for ch in word:
            freqncy[ord(ch) - ord('a')] += 1
        return freqncy
    
    def intersection(self, freq1, freq2):
        return [min(f1, f2) for f1, f2 in zip(freq1, freq2)]
    
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        last = self.count(words[0])

        for word in words[1:]:
            last = self.intersection(last, self.count(word))
        
        res = []
        for i in range(26):
            res.extend([chr(i + ord('a'))] * last[i])

        return res

        '''
        Original
        def findNumchar(string):
            num_char = {}
            for ch in string:
                if ch in num_char:
                    num_char[ch] += 1
                else:
                    num_char[ch] = 1
            return num_char
        
        num_char = findNumchar(words[0])

        for i in range(1, len(words)):
            temp = []
            for ch in words[i]:
                if ch in num_char and num_char[ch] > 0:
                    num_char[ch] -= 1
                    temp.append(ch)
            num_char = findNumchar(temp)

        res = []
        for ch, count in num_char.items():
            res = sum([[ch] * count], res)
        return res
        '''