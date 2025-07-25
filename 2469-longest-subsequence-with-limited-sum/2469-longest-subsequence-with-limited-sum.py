class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
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