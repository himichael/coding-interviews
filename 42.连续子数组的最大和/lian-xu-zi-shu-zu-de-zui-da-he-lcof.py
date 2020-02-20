class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""	
		if not nums:
			return 0
		res = nums[0]
		sum = 0
		for i in nums:
			if sum>=0:
				sum += i
			else:
				sum = i
			res = max(res,sum)
		return res