class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fiveDollar = 0
        tenDollar = 0

        for bill in bills:
            if bill == 5:
                fiveDollar += 1
            elif bill == 10:
                if fiveDollar > 0:
                    fiveDollar -= 1
                else:
                    return False
                tenDollar += 1
            else:
                if fiveDollar > 0 and tenDollar > 0:
                    fiveDollar -= 1
                    tenDollar -= 1
                elif fiveDollar > 2:
                    fiveDollar -= 3
                else:
                    return False
        return True
