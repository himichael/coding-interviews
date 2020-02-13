class Solution(object):
	def findNumberIn2DArray(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not (matrix and matrix[0]):
			return False
		n = len(matrix)
		m = len(matrix[0])
		i = n-1
		j = 0
		while i>=0 and j<m:
			if matrix[i][j]>target:
				i -= 1
			elif matrix[i][j]<target:
				j += 1
			else:
				return True
		return False