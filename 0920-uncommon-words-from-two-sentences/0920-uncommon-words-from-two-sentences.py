class Solution(object):
    from collections import Counter
    '''
    def uniqueWord(self, str1, str2):
        unique = []
        for word in str1:
            if str1[word] == 1 and word not in str2:
                unique.append(word)
        return unique
    '''
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        '''
        s1 = Counter(s1.split())
        s2 = Counter(s2.split())
        uncommonWords = []
        uncommonWords += self.uniqueWord(s1, s2)
        uncommonWords += self.uniqueWord(s2, s1)
        return uncommonWords

        '''

        str = Counter(s1.split() + s2.split())
        uniqueWords = []
        for word in str:
            if str[word] == 1:
                uniqueWords.append(word)
        return uniqueWords
        