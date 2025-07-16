class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        dic = {}
        for word in s:
            dic[word[-1]] = word[:-1] # word[-1] returns the last character of the string
        
        return ' '.join([dic[i] for i in sorted(dic)])