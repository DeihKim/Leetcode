class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.findall(r'\w+', paragraph.lower())
        freqncy = Counter(words)
        for word, _ in freqncy.most_common():
            if word not in banned:
                return word

