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
		
	# 快速选择
	def getLeastNumbers(self, arr, k):
		if not arr or k<=0:
			return []
		if len(arr)<=k:
			return arr
		def partitioin(begin,end):
			povit = arr[end]
			i = begin
			for j in xrange(begin,end):
				if arr[j]<povit:
					arr[i],arr[j] = arr[j],arr[i]
					i += 1
			arr[i],arr[end] = arr[end],arr[i]
			return i
		def quick_search(begin,end,k):
			if begin>=end:
				return
			pos = partitioin(begin,end)
			if pos>k:
				quick_search(begin,pos-1,k)
			elif pos<k:
				quick_search(pos+1,end,k)
			else:
				return
		quick_search(0,len(arr)-1,k)
		return arr[:k]
		
		