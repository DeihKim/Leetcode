class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxWord = 0
        for s in sentences:
            maxWord = max(maxWord, len(s.split()))
        return maxWord