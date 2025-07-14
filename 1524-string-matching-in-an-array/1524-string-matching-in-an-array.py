class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(words)
        res = set()
        for i, word in enumerate(words):
            for j in range(n):
                if i != j and word in words[j]:
                    res.add(word)
        return list(res)