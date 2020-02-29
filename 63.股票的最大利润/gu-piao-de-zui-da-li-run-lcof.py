class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		dp = [[0 for _ in xrange(2)] for _ in xrange(n)]
		dp[0][0] = 0
		dp[0][1] = -prices[0]
		res = 0
		for i in xrange(1,n):
			dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
			dp[i][1] = max(dp[i-1][1],-prices[i])
			res = max(res,dp[i][0],dp[i][1])
		return res
		
		
		
# 动态规划，状态压缩		
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		dp0 = 0
		dp1 = -prices[0]
		res = 0
		for i in xrange(1,n):
			dp0 = max(dp0,dp1+prices[i])
			dp1 = max(dp1,-prices[i])
			res = max(res,dp0,dp1)
		return res	

		