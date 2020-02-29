class Solution(object):
	def strToInt(self, str):
		"""
		:type str: str
		:rtype: int
		"""
		if not str:
			return 0
		n = len(str)
		i = 0
		res = 0
		while i<n and str[i]==' ':
			i += 1
		if i==n:
			return 0
		is_negative = True if str[i]=='-' else False
		if str[i] in ('-','+'):
			i += 1
		while i<n and str[i]>='0' and str[i]<='9':
			tmp = ord(str[i])-ord('0')
			if not is_negative and (res>214748364 or (res==214748364 and tmp>=7)):
				return 2147483647
			if is_negative and (-res<-214748364 or (-res==-214748364 and tmp>=8)):
				return -2147483648
			res = res*10 + tmp
			i += 1
		return -res if is_negative else res