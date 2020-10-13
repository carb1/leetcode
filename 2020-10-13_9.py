class Solution:
    """
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:

    输入: 121
    输出: true
    示例 2:

    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
    示例 3:

    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。
    """
    def isPalindrome(self, x: int) -> bool:
        floor = 0
        ceil = -1
        s = str(x)
        while floor + abs(ceil) + 1 <= len(s):
            if s[floor] == s[ceil]:
                floor += 1
                ceil -= 1
            else:
                return False
        return True

    def isPalindrome_2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome(112))
