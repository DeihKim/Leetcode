class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #To form a triangle, sum of two shorter sides must be greater than the longest side

        #sort the list in a descending order
        nums.sort(reverse = True)

        #remove the longest side til it is less than the sum of two shorter sides
        #as long as there are two sides left
        while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
            nums.pop(0)

        #less than 3 sides are left
        if len(nums) < 3:
            return 0
        #return the sum of the first three sum
        else:
            return sum(nums[:3]) # nums[:3] returns the list stopping at index 3