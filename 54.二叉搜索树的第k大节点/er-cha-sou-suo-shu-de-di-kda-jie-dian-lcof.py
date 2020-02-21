class Solution(object):
	def kthLargest(self, root, k):
		if not root:
			return 0
		self.res = 0
		self.index = 0
		def dfs(root):
			if not root:
				return
			dfs(root.right)
			self.index += 1
			if self.index==k:
				self.res = root.val
				return
			dfs(root.left)
		dfs(root)
		return self.res