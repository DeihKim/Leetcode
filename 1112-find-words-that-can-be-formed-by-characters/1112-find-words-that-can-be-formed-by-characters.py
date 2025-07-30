class Solution(object):
    from collections import Counter
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        def canForm(self, word, alphaCount):
            wCount = [0] * 26
            for ch in word:
                indx = ord(ch) - ord('a')
                wCount[indx] += 1
                if wCount[indx] > alphaCount[indx]:
                    return False
            return True
            
        alphaCount = [0] * 26
        for ch in chars:
            alphaCount[ord(ch) - ord('a')] += 1
        
        total = 0
        for word in words:
            if canForm(self, word, alphaCount):
                total += len(word)
        
        return total
        
        '''Original
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
        '''