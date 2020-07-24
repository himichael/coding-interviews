class Solution(object):
    def minArray(self, numbers):
        begin = 0
        end = len(numbers)-1
        while begin<=end:
            mid = begin+(end-begin)//2
            if numbers[mid]>numbers[end]:
                begin = mid+1
            elif numbers[mid]<numbers[end]:
                end = mid
            else:
                end -= 1
        return numbers[begin]