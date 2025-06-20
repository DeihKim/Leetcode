class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ogNums = len(nums)
        i = 0
        pop = 0
        for j in range(len(nums)):
            if nums[i] % 2 != 0:
                nums.pop(i)
                pop += 1
            else:
                i += 1

        if pop == ogNums:
            return -1
        
        elif len(nums) == 1:
            return nums[0]

        else:
            mostFqnt = 1
            fqnt = 1
            Maxelemnt = nums[0]
            elemnt = nums[0]
            for i in range(1, len(nums)):
                if nums[i] == elemnt:
                    fqnt += 1
                    if mostFqnt < fqnt:
                        mostFqnt = fqnt
                        Maxelemnt = nums[i]
                else:
                    elemnt = nums[i]
                    fqnt = 1
        return Maxelemnt
                