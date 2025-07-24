class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        even = []
        odd = []
        for i in str(num):
            i = int(i)
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        even.sort(reverse = True)
        odd.sort(reverse = True)

        evenIndex = 0
        oddIndex = 0
        res = ""
        for i in str(num):
            if int(i) % 2 == 0:
                res += str(even[evenIndex])
                evenIndex += 1
            else:
                res += str(odd[oddIndex])
                oddIndex += 1
        return int(res)
        