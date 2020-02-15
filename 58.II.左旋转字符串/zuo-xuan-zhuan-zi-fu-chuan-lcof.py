class Solution(object):
	def reverseLeftWords(self, s, n):
		"""
		:type s: str
		:type n: int
		:rtype: str
		"""
		size = len(s)
		return s[n:size]+s[0:n]
		
	def reverseLeftWords(self, s, n):
		"""
		:type s: str
		:type n: int
		:rtype: str
		"""
		return s[n:]+s[:n]		