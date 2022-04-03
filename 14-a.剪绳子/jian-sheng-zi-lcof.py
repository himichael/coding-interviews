class Solution(object):
    def cuttingRope(self, n):
        if n <= 1:
            return 0 if n == 0 else 1
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            tmp = 0
            for j in range(1, i):
                tmp = max(tmp, j * (i - j), j * dp[i - j])
            dp[i] = tmp
        return dp[-1]