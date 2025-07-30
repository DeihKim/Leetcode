class Solution(object):
    from collections import Counter
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        alphabet = [0] * 26
        for c in ransomNote:
            indx = ord(c) - ord('a')
            i = magazine.find(c, alphabet[indx])
            if i == -1:
                return False
            alphabet[indx] = i + 1
        return True
        '''
        Original
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for char in ransomNote:
            if ransomNote[char] > magazine[char]:
                return False
        return True
        '''