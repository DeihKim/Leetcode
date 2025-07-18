class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix) and prefix:
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix

        '''
        compareLen = len(strs[0])
        for i in range(compareLen):
            check = strs[0][:compareLen - i]
            common = all(s.startswith(check) for s in strs)
            if common:
                return check
        return ""
        '''