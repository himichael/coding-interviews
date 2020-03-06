class Solution(object):
	def permutation(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		res = set()
		def dfs(queue,stack):
			if not queue:
				res.add("".join(stack))
				return
			size = len(queue)
			for _ in xrange(size):
				stack.append(queue.pop(0))
				dfs(queue,stack)
				queue.append(stack.pop())
		dfs(list(s),[])
		return list(res)