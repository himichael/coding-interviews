class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		queue = [root]
		res = []
		while queue:
			size = len(queue)
			for _ in xrange(size):
				tmp = queue.pop(0)
				res.append(tmp.val)
				if tmp.left:
					queue.append(tmp.left)
				if tmp.right:
					queue.append(tmp.right)
		return res