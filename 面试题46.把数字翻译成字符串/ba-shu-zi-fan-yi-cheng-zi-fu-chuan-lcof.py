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