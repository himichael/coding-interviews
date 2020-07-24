class Solution(object):
	def translateNum(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		if not num:
			return 1
		nums = str(num)
		n = len(nums)
		def dfs(index):
			if index>=n:
				return 1
			if index==n-1:
				return dfs(index+1)
			s = int(nums[index:index+2])
			if s>=10 and s<=25:
				return dfs(index+1) + dfs(index+2)
			return dfs(index+1)
		return dfs(0)
		
		
		
	# 动态规划实现
	def translateNum(self, num):
		if num<10:
			return 1
		s = str(num)
		n = len(s)
		def check(s1,s2):
			s = int(s1+s2)
			if s>=10 and s<=25:
				return True
			return False
		dp = [0 for _ in xrange(n)]
		dp[0] = 1
		dp[1] = 2 if check(s[0],s[1]) else 1
		for i in xrange(2,n):
			if check(s[i-1],s[i]):
				dp[i] = dp[i-1] + dp[i-2]
			else:
				dp[i] = dp[i-1]
		return dp[-1]
		
		