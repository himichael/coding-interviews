class Solution(object):
	def myPow(self, x, n):
		if n==0:
			return 1.0
		if n==1:
			return x
		if n<0:
			return 1/self.myPow(x,n*-1)
		if n%2==1:
			return x * self.myPow(x,n-1)
		else:
			return self.myPow(x*x,n/2)