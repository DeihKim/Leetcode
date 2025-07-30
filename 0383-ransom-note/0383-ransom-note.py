class Solution(object):
    from collections import Counter
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for char in ransomNote:
            if ransomNote[char] > magazine[char]:
                return False
        return True