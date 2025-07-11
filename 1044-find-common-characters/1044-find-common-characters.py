class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def findNumchar(string):
            num_char = {}
            for ch in string:
                if ch in num_char:
                    num_char[ch] += 1
                else:
                    num_char[ch] = 1
            return num_char
        
        num_char = findNumchar(words[0])

        for i in range(1, len(words)):
            temp = []
            for ch in words[i]:
                if ch in num_char and num_char[ch] > 0:
                    num_char[ch] -= 1
                    temp.append(ch)
            num_char = findNumchar(temp)

        res = []
        for ch, count in num_char.items():
            res = sum([[ch] * count], res)
        return res