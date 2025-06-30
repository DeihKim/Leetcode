class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        currentOccupy = 0
        maxOccupy = 0
        for i in s:
            if i == "E":
                currentOccupy += 1
            else:
                currentOccupy -= 1
            
            if maxOccupy < currentOccupy:
                maxOccupy = currentOccupy
        return maxOccupy