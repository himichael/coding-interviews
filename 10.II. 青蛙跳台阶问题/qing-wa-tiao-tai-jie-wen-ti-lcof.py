class Solution(object):
	def numWays(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n==0:
			return 1
		f1 = 1
		f2 = 1
		for i in xrange(2,n+1):
			tmp = f1+f2
			f1 = f2
			f2 = tmp
		return f2%1000000007