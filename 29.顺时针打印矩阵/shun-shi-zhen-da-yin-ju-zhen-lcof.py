class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if not matrix:
			return []
		res = []
		r1 = 0
		r2 = len(matrix)-1
		c1 = 0
		c2 = len(matrix[0])-1
		while r1<=r2 and c1<=c2:
			for i in xrange(c1,c2+1):
				res.append(matrix[r1][i])
			for i in xrange(r1+1,r2+1):
				res.append(matrix[i][c2])
			if r1<r2 and c1<c2:
				for i in xrange(c2-1,c1,-1):
					res.append(matrix[r2][i])
				for i in xrange(r2,r1,-1):
					res.append(matrix[i][c1])
			r1 += 1
			r2 -= 1
			c1 += 1
			c2 -= 1
		return res