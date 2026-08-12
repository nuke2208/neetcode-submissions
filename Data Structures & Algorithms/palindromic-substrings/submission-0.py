class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = 0
        maxlength = 1
        for i in range(n):
            dp[i][i] = True
        for length in range(2,n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] is True:
                    if length > maxlength:
                        count = count + 1
        return count + n
        