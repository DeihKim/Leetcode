class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        freq1 = self.countFreq(s)
        freq2 = self.countFreq(target)
        
        copy = float('inf')
        for pair in zip(freq1, freq2):
            if pair[1] != 0:
                copy = min(copy, pair[0] / pair[1])
        
        return copy

    def countFreq(self, string):
        freq = [0] * 26
        for char in string:
            freq[ord(char) - ord('a')] += 1
        return freq