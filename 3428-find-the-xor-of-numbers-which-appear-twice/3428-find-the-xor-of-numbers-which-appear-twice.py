class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hset = {}
        for i in range(len(nums)):
            if nums[i] in hset:
                hset[nums[i]] += 1
            else:
                hset[nums[i]] = 1

        xor = 0
        for num in hset:
            if hset[num] == 2:
                xor ^= num
        return xor