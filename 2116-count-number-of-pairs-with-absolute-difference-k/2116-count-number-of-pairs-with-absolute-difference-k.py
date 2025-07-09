class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freqncy = {}
        for num in nums:
            if num in freqncy:
                freqncy[num] += 1
            else:
                freqncy[num] = 1
        
        count = 0
        for num in nums:
            if num + k in freqncy:
                count += freqncy[num + k]
        return count
        
        '''
        seen = defaultdict(int)
        count = 0
        for num in nums:
            # this adds all valid previous matches in one go
            # e.g: num = 2, k = 1
            # so num - k = 2 - 1 = 1 and num + k = 2 + 1 = 3
            count += seen[num - k] + seen[num + k]
            seen[num] += 1
        return count
        '''

        '''
        Original
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) == k:
                    count += 1
        return count
        '''