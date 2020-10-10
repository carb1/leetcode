class Solution:
    """
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

    示例 1:

    输入: 123
    输出: 321
     示例 2:

    输入: -123
    输出: -321
    示例 3:

    输入: 120
    输出: 21
    """

    def reverse(self, x: int) -> int:
        s = str(x)
        sign = True
        if s[0] == '-':
            s = s[1:]
            sign = False
        lst = []
        for i in s:
            lst.append(i)
        lst.reverse()
        num = int(''.join(lst))
        import math
        if num > math.pow(2, 31) - 1:
            return 0
        if sign:
            return num
        else:
            return num * -1

    def reverse_2(self, x: int) -> int:
        if -10 < x < 10:
            return x
        s = str(x)
        if s[0] == '-':
            num = int(s[:0:-1])
            num = num * -1
        else:
            num = int(s[::-1])
        return num if -2147483648 < num < 2147483647 else 0

    def reverse_3(self, x: int) -> int:
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res


if __name__ == '__main__':
    test = Solution()
    print(test.reverse_3(-1534469))

