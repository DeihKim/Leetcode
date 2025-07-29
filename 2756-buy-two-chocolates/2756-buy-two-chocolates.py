class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        minPrice = float('inf')
        sminPrice = float('inf')
        for i in range(len(prices)):
            if prices[i] < minPrice:
                sminPrice = minPrice
                minPrice = prices[i]
            elif prices[i] < sminPrice:
                sminPrice = prices[i]
        cost = minPrice + sminPrice
        if cost <= money:
            return money - cost
        return money

        '''
        Original
        prices.sort()
        if prices[0] + prices[1] <= money:
            return money - (prices[0] + prices[1])
        return money
        '''