class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        s = s.split()
        res = [''] * len(s)
        for i in s:
            indx = int(i[-1]) - 1
            res[indx] = i[:-1]
        return ' '.join(res)
        '''

        s = s.split()
        dic = {}
        for word in s:
            dic[word[-1]] = word[:-1] # word[-1] returns the last character of the string
        
        return ' '.join([dic[i] for i in sorted(dic)])