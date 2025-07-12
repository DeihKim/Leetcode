class Solution(object):
    from collections import Counter

    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        words1 = Counter(words1)
        words2 = Counter(words2)
        count = 0
        for word in words1:
            if words1[word] == 1 and words2[word] == 1:
                count += 1
        return count