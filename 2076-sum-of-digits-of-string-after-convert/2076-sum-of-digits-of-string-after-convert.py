class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        convert = "".join(str(ord(ch) - 96) for ch in s)
        for i in range(k):
            total = sum(map(int, convert))
            convert = str(total)
        return total

        '''
        Original
        convert = ""
        for char in s:
            convert += str(ord(char) - ord('a') + 1)
        
        total = 0
        for i in range(k):
            total = sum(int(num) for num in convert)
            convert = str(total)
        return total
        '''  