class Solution(object):
	# 利用大根堆，注意python默认只有小根堆，需要将元素取反再放入
	def getLeastNumbers(self, arr, k):
		if not arr or k<=0:
			return []
		if len(arr)<=k:
			return arr
		import heapq
		queue = [-i for i in arr[:k]]
		heapq.heapify(queue)
		for i in xrange(k,len(arr)):
			if -queue[0]>arr[i]:
				heapq.heappop(queue)
				heapq.heappush(queue,-arr[i])
		for i in xrange(k):
			queue[i] *= -1
		return queue