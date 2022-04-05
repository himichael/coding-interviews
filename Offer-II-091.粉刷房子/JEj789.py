class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        d = {}
        def dfs(stats, index):
            if index == n:
                return 0
            if (stats, index) in d:
                return d[stats, index]
            a = dfs( (stats + 1) % 3, index + 1) + costs[index][stats]
            b = dfs( (stats + 2) % 3, index + 1) + costs[index][stats]
            d[stats, index] = min(a, b)
            return d[stats, index]
        res = min(dfs(0, 0), dfs(1, 0), dfs(2, 0))
        return res
            
			

	# 动态规划解法
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        cols = 3
        dp = [[float("inf") for _ in range(cols)] for _ in range(n)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        for i in range(1, n):
            for j in range(cols):
                a = dp[i - 1][(j + 1) % cols] + costs[i][j]
                b = dp[i - 1][(j + 2) % cols] + costs[i][j]
                dp[i][j] = min(a, b)
        return min(dp[-1][j] for j in range(cols))
		
		
		
	# 数组空间优化
    def minCost(self, costs):
        n = len(costs)
        a = costs[0][0]
        b = costs[0][1]
        c = costs[0][2]
        for i in range(1, n):
            x = min(b, c) + costs[i][0]
            y = min(a, c) + costs[i][1]
            z = min(a, b) + costs[i][2]
            a,b,c = x,y,z
        return min(a,b,c)

		
		
		