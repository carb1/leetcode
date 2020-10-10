class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 k=i+l 得到子串的结束位置
            for i in range(n):
                k = i + l
                if k >= len(s):
                    break
                if l == 0:
                    dp[i][k] = True
                elif l == 1:
                    dp[i][k] = (s[i] == s[k])
                else:
                    dp[i][k] = (dp[i + 1][k - 1] and s[i] == s[k])
                if dp[i][k] and l + 1 > len(ans):
                    ans = s[i:k+1]
        return ans