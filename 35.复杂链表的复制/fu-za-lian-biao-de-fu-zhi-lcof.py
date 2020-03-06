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
		
		
		
	def copyRandomList(self, head):
		"""
		:type head: Node
		:rtype: Node
		"""
		p1,p2 = head,head
		d = dict()
		while p1:
			d[p1] = Node(p1.val,None,None)
			p1 = p1.next
		while p2:
			d[p2].next = d[p2.next] if p2.next else None
			d[p2].random = d[p2.random] if p2.random else None
			p2 = p2.next
		return d[head] if head else None		