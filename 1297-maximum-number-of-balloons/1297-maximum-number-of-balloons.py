class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b = text.count('b')
        a = text.count('a')
        l = text.count('l') / 2
        o = text.count('o') / 2
        n = text.count('n')
        return min(b, a, l, o, n)
        
        '''
        Origianl
        freq1 = self.countFreq(text)
        freq2 = self.countFreq("balloon")

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
        '''