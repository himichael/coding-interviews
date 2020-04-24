class Solution(object):
	def reversePairs(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""		
		if not nums:
			return 0
		if len(nums)<2:
			return 0
		tmp = [0 for _ in xrange(len(nums))]
		return self.count_reverse_pairs(nums,0,len(tmp)-1,tmp)
		
	def count_reverse_pairs(self,nums,left,right,tmp):
		if left==right:
			return 0
		mid = left+(right-left)/2
		left_pairs = self.count_reverse_pairs(nums,left,mid,tmp)
		right_pairs = self.count_reverse_pairs(nums,mid+1,right,tmp)
		if nums[mid]<=nums[mid+1]:
			return left_pairs + right_pairs
		cross_pairs = self.merge_and_cont(nums,left,mid,right,tmp)
		return cross_pairs + left_pairs + right_pairs
		
	def merge_and_cont(self,nums,left,mid,right,tmp):
		for i in xrange(left,right+1):
			tmp[i] = nums[i]
		i = left
		j = mid+1
		count = 0
		for k in xrange(left,right+1):
			if i>mid:
				nums[k] = tmp[j]
				j += 1
			elif j>right:
				nums[k] = tmp[i]
				i += 1
			elif tmp[i]<=tmp[j]:
				nums[k] = tmp[i]
				i += 1
			else:
				nums[k] = tmp[j]
				j += 1
				count += (mid-i+1)
		return count