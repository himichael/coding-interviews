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