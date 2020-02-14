class Solution(object):
	def sumNums(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return n>0 and n+self.sumNums(n-1)