class Solution(object):
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True
		def dfs(root):
			if not root:
				return 0
			left = dfs(root.left)
			right = dfs(root.right)
			return max(left,right)+1
		r = abs(dfs(root.left)-dfs(root.right))<=1
		left = self.isBalanced(root.left)
		right = self.isBalanced(root.right)
		return r and left and right