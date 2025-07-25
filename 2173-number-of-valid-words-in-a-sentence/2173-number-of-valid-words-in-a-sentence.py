class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        def valid(word):
            seen = False
            for i, char in enumerate(word):
                if char.isdigit() or (char in "!.," and i != len(word) - 1):
                    return False
                elif char == '-':
                    if seen or i == 0 or i == len(word) - 1 or not word[i + 1].isalpha():
                        return False
                    seen = True
            return True
        
        return sum(valid(word) for word in sentence.split())