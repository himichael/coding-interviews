class Solution(object):
	def copyRandomList(self, head):
		"""
		:type head: Node
		:rtype: Node
		"""
		p1,p2,p3 = head,head,head
		p = Node(-1,None,None)
		cur = p
		while p1:
			tmp = Node(p1.val,None,None)
			tmp.next = p1.next
			p1.next = tmp
			p1 = tmp.next
		while p2:
			tmp = p2.next
			tmp.random = p2.random.next if p2.random else None
			p2 = tmp.next
		while p3:
			cur.next = p3.next
			cur = cur.next
			p3.next = cur.next
			p3 = p3.next
		return p.next