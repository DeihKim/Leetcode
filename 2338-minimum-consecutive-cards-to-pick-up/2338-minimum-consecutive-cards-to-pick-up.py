class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        left = 0
        minCards = float('inf')
        nums = set()
        for right in range(len(cards)):
            while cards[right] in nums:
                minCards = min(minCards, right - left + 1)
                nums.remove(cards[left])
                left += 1
            nums.add(cards[right])
        
        return minCards if minCards != float('inf') else -1
            