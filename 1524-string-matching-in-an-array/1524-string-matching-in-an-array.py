class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res
        '''
        Original
        n = len(words)
        res = set()
        for i, word in enumerate(words):
            for j in range(n):
                if i != j and word in words[j]:
                    res.add(word)
        return list(res)
        '''