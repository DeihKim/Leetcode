class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sList = s.split()
        if len(pattern) != len(sList):
            return False
        
        char_word = {}
        word_char = {}

        for char, word in zip(pattern, sList):
            if char in char_word:
                if char_word[char] != word:
                    return False
            else:
                if word in word_char:
                    return False
                char_word[char] = word
                word_char[word] = char
        
        return True
