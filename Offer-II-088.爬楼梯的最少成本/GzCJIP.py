class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost or len(cost) <= 2:
            return 0 if not cost else min(cost[0], cost[1])
        n = len(cost)
        pre = 0
        cur = 0
        for i in range(2, n):
            tmp = min(pre + cost[i - 2], cur + cost[i - 1])
            pre = cur
            cur = tmp
        return min(pre + cost[-2], cur + cost[-1])
		
		
	# 递归实现
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        d = {}
        def dfs(index):
            if index in d:
                return d[index]
            if index <= 1:
                return 0
            a = dfs(index - 1) + cost[index - 1]
            b = dfs(index - 2) + cost[index - 2]
            d[index] = min(a, b)
            return d[index]
        return dfs(n)