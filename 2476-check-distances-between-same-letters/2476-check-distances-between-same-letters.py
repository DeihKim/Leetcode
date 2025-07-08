class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        char = set(s)
        for c in char:
            index = s.index(c)
            dis = distance[ord(c) - 97] #unicode of a is 97
            if index + dis + 1 > len(s) - 1 or s[index + dis + 1] != c:
                return False
        return True