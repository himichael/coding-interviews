class Solution(object):
	def movingCount(self, m, n, k):
		"""
		:type m: int
		:type n: int
		:type k: int
		:rtype: int
		"""
		dx = [0,1,0,-1]
		dy = [1,0,-1,0]
		cache = set()
		def sum(i,j):
			res = 0
			while i>0 or j>0:
				res += i%10 + j%10
				i //= 10
				j //= 10
			return res
		def dfs(i,j):
			if 0>i or i==m or 0>j or j==n or sum(i,j)>k or (i,j) in cache:
				return 
			cache.add((i,j))
			for step in xrange(4):
				x = i + dx[step]
				y = j + dy[step]
				dfs(x,y)
		dfs(0,0)
		return len(cache)