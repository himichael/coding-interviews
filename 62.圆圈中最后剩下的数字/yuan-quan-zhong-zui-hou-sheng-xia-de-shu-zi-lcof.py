class Solution(object):
	# 约瑟夫环，用数组模拟
	def lastRemaining(self, n, m):
		"""
		:type n: int
		:type m: int
		:rtype: int
		"""
		if n<=0 or m<=0:
			return 0
		arr = [i for i in xrange(n)]
		idx = 0
		m -= 1
		while len(arr)>1:
			idx = (idx+m)%n
			arr.pop(idx)
			n -= 1
		return arr[0]
		
		
		
	# 数学解法
	def lastRemaining(self, n, m):
		if n<=0 or m<=0:
			return 0
		res = 0
		for i in xrange(2,n+1):
			res = (res+m)%i
		return res