class Solution(object):
	def replaceSpace(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if not s:
			return s
		arr = list(s)
		for i in xrange(len(arr)):
			if arr[i]==' ':
				arr[i] = '%20'
		return "".join(arr)
		


    def replaceSpace(self, s):
        return s.replace(" ","%20")
		
		
		