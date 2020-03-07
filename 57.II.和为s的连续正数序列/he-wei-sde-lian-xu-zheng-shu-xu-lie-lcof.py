class Solution(object):
	def findContinuousSequence(self, target):
		if target<=0:
			return []
		res = []
		for i in xrange(1,target+1):
			tmp = [i]
			x = i
			for j in xrange(i+1,target+1):
				x += j
				tmp.append(j)
				if x==target and len(tmp)>1:
					res.append(tmp)
					break
				if x>target:
					break
		return res
		
		
		
	# 双指针+求根公式优化
	def findContinuousSequence(self, target):
		i = 1
		j = 2
		res = []
		while i<j:
			tmp = (i+j)*(j-i+1)/2
			if tmp==target:
				arr = [k for k in xrange(i,j+1)]
				res.append(arr)
				i += 1
			elif tmp<target:
				j += 1
			else:
				i += 1
		return res
		