class Solution(object):
	def singleNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""		
		if not nums:
			return [-1,-1]
		ans = 0
		for n in nums:
			ans ^= n
		div = 1
		while (div&ans)==0:
			div <<= 1
		a = 0
		b = 0
		for n in nums:
			if n&div:
				a ^= n
			else:
				b ^= n
		return [a,b]