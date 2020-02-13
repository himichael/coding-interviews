class Solution(object):
	def reversePrint(self, head):
		"""
		:type head: ListNode
		:rtype: List[int]
		"""
		res = []
		while head:
			res.insert(0,head.val)
			head = head.next
		return res