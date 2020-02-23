class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		res = []
		def dfs(index,root):
			if not root:
				return
			if len(res)<index:
				res.append([])
			res[index-1].append(root.val)
			dfs(index+1,root.left)
			dfs(index+1,root.right)
		dfs(1,root)
		return res