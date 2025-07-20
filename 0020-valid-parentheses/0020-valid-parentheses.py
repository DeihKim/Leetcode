class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in parentheses:
                if stack and stack[-1] == parentheses[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack