class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        freq = defaultdict(int)
        maxFreq = 0

        for i in range(len(s) - minSize + 1):
            substring = s[i: i + minSize]
            if len(set(substring)) <= maxLetters:
                freq[substring] += 1
                maxFreq = max(maxFreq, freq[substring])
        
        return maxFreq