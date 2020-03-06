class MinStack(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.data = []
		self.inner = []

	def push(self, x):
		"""
		:type x: int
		:rtype: None
		"""
		if len(self.inner)==0 or x<=self.inner[-1]:
			self.inner.append(x)
		self.data.append(x)

	def pop(self):
		"""
		:rtype: None
		"""
		tmp = self.data.pop()
		if tmp==self.inner[-1]:
			self.inner.pop()

	def top(self):
		"""
		:rtype: int
		"""
		return self.data[-1]

	def min(self):
		"""
		:rtype: int
		"""
		return self.inner[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()