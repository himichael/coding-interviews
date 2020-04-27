class Solution(object):
	# DFS实现 
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
		
		
		
	# 广度优先实现
	def movingCount(self, m, n, k):
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
		queue = [(0,0)]
		while queue:
			i,j = queue.pop(0)
			if 0>i or i==m or 0>j or j==n or sum(i,j)>k or (i,j) in cache:
				continue
			cache.add((i,j))
			for step in xrange(4):
				x = i + dx[step]
				y = j + dy[step]
				queue.append((x,y))
		return len(cache)
		
		
		
	# BFS的另一种写法
	def movingCount(self, m, n, k):		
		def vaild(i,j):
			ans = 0
			while i>0:
				ans += i%10
				i //= 10
			while j>0:
				ans += j%10
				j //= 10
			return ans<=k
		queue = [(0,0)]
		cache = set()
		direct = ((0,1),(1,0))
		queue.append((0,0))
		while queue:
			x, y = queue.pop(0)
			if 0<=x<m and 0<=y<n and (x,y) not in cache and vaild(x,y):
				cache.add((x,y)) 
				# for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
				for dx, dy in [(1,0),(0,1)]: 	 # 仅考虑向右和向下即可
					queue.append((x+dx,y+dy)) 
		return len(cache)