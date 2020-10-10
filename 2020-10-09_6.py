class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        lst = ['' for _ in range(numRows)]
        swap = -1
        line = 0
        for i in s:
            lst[line] += i
            if (line == numRows - 1) or (line == 0):
                swap = -swap
            line += swap
        return ''.join(lst)


if __name__ == '__main__':
    test = Solution()
    print(test.convert('LEETCODEISHIRING', 3))