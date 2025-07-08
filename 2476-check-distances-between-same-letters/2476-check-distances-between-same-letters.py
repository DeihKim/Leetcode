class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        char = set(s)
        for c in char:
            index = s.index(c) # return the index where c first occurs
            
            # return the distance of the letter c in the distance array
            dis = distance[ord(c) - 97] # unicode of a is 97

            # check if the the index might be out of range
            # check if the second occurance of c is in the correct place
            if index + dis + 1 > len(s) - 1 or s[index + dis + 1] != c:
                return False
        return True