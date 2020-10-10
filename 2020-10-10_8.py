class Solution:
    def myAtoi(self, s: str) -> int:
        lst = []
        if s[0] == ' ' or s[0].isnumeric():
            for i in s:
                if i.isnumeric():
                    lst.append(i)
                elif i == ' ':
                    continue
                else:
                    break
        else:
            return 0
        return lst


if __name__ == '__main__':
    test = Solution()
    print(test.myAtoi('-12321'))
