class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        dp = [0]*(n+1)
        if n>=1:
            dp[0] = 1
            dp[1] = 1
        for i in range(2,n+1):
            onedigit = s[i-1]
            twodigit = s[i-2] + s[i-1]
            if '1' <= onedigit <= '9':
                dp[i] = dp[i-1]
            if '10' <= twodigit <= '26':
                dp[i] = dp[i] + dp[i-2]
        return dp[n]
        