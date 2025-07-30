class Solution(object):
    from collections import Counter
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars = Counter(chars)
        total = 0
        for word in words:
            wordf = Counter(word)
            good = True
            for c in word:
                if wordf[c] > chars[c]:
                    good = False
            if good:
                total += len(word)
        return total