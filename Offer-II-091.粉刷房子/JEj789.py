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
            