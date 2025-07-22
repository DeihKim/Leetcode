class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = float('inf')
        for num in nums:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            if total < min:
                min = total
        return min
        '''
        Original
        replaced = []
        for num in nums:
            replaced.append(sum(map(int, str(num))))
        return min(replaced)
        '''