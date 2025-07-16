class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        goodString = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']
        for sub in goodString:
            if sub in num:
                return sub
        return ''