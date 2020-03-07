class MaxQueue(object):
	def __init__(self):
		import collections
		self.queue = collections.deque()
		self.inner = collections.deque()

	def max_value(self):
		"""
		:rtype: int
		"""
		if not self.inner:
			return -1
		return self.inner[0]

	def push_back(self, value):
		"""
		:type value: int
		:rtype: None
		"""
		self.queue.append(value)
		while self.inner and self.inner[-1]<value:
			self.inner.pop()
		self.inner.append(value)
		

	def pop_front(self):
		"""
		:rtype: int
		"""
		if not self.queue:
			return -1
		res = self.queue.popleft()
		if res==self.inner[0]:
			self.inner.popleft()
		return res
			


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()