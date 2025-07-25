class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        total = [0] * len(nums)
        total[0] = nums[0]
        for i in range(1, len(nums)):
            total[i] = total[i - 1] + nums[i]
        
        res = []
        for query in queries:
            index = bisect.bisect(total, query)
            res.append(index)
        return res

        '''
        original
        nums.sort()
        total = []
        sum = 0
        for num in nums:
            sum += num
            total.append(sum)

        ans = []
        for query in queries:
            count = 0
            for num in total:
                if num <= query:
                    count += 1
                else:
                    break
            ans.append(count)
        return ans
        '''