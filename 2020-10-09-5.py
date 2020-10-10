class Solution:
    """
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

    示例 1：

    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
    示例 2：

    输入: "cbbd"
    输出: "bb"
    """
    def longestPalindrome(self, s: str) -> str:
        """
        动态规划
        """
        ans = ''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                k = j + i
                if k >= len(s):
                    break
                if i == 0:
                    dp[j][k] = True
                elif i == 1:
                    dp[j][k] = (s[j] == s[k])
                else:
                    dp[j][k] = (dp[j + 1][k - 1] and s[j] == s[k])
                if dp[j][k] and i + 1 > len(ans):
                    ans = s[j: k + 1]
        return ans


if __name__ == '__main__':
    test = Solution()
    print(test.longestPalindrome("babad"))
