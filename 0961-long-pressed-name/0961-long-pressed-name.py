class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        count = 0
        for i in range(len(typed)):
            if count < len(name) and typed[i] == name[count]:
                count += 1
            elif count == 0 or typed[i] != name[count - 1]:
                return False
        return count == len(name)