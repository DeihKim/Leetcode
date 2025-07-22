class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_t = {}
        t_s = {}

        for sWord, tWord in zip(s, t):
            if sWord in s_t:
                if s_t[sWord] != tWord:
                    return False
            else:
                if tWord in t_s:
                    return False
                s_t[sWord] = tWord
                t_s[tWord] = sWord
        
        return True