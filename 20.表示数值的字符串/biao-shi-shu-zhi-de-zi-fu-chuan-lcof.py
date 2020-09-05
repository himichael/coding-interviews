class Solution(object):
    def isNumber(self, s):
        if not s:
            return False
        n = len(s)
        i = 0
        j = n-1
        while i<n and s[i]==" ":
            i += 1
        while j>=0 and s[j]==" ":
            j -= 1
        s = s[i:j+1]
        if not s:
            return False
        i = 0
        n = len(s)
        if s[i]=="+" or s[i]=="-":
            i += 1
            if i==n:
                return False
        letter = set(["0","1","2","3","4","5","6","7","8","9","."])
        dot_num = 0
        digit_num = 0
        while i<n and s[i] in letter:
            if s[i]==".":
                dot_num += 1
            else:
                digit_num += 1
            i += 1
        if i==n:
            if dot_num<=1:
                return digit_num>0
            return False
        letter.remove(".")
        if s[i]=="e" or s[i]=="E":
            if dot_num>1 or digit_num==0:
                return False
            i += 1
            if i==n:
                return False
            if s[i]=="+" or s[i]=="-":
                i += 1
                if i==n:
                    return False
            digit_num = 0
            while i<n and s[i] in letter:
                digit_num += 1
                i += 1
            if i==n:
                if digit_num==0:
                    return False
                return True
        return False