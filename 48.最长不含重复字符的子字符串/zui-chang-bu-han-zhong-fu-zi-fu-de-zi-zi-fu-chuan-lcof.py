class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		d = dict()
		left = 0
		res = 0
		for i in xrange(len(s)):
			if s[i] in d:
				left = max(left,d[s[i]]+1)
			d[s[i]] = i
			res = max(res,i-left+1)
		return res
		
		
		
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		letters = set()
		i,j,n = 0,0,len(s)
		res = 0
		while i<n and j<n:
			if s[j] not in letters:
				letters.add(s[j])
				j += 1
				res = max(res,j-i)
			else:
				letters.remove(s[i])
				i += 1
		return res