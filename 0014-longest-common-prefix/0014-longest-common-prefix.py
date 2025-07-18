class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        compareLen = len(strs[0])
        for i in range(compareLen):
            check = strs[0][:compareLen - i]
            common = all(s.startswith(check) for s in strs)
            if common:
                return check
        return ""