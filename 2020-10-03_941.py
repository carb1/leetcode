class Solution:
    def validMountainArray(self, A) -> bool:
        if not A: return False
        n = len(A)
        if n == 1: return False
        sign = ' '
        i = 0
        while i < n - 1:
            if A[i + 1] > A[i]:
                if sign == ' ':
                    sign = 'up'
                    i += 1
                elif sign == 'up':
                    i += 1
                else:
                    return False
            elif A[i + 1] < A[i]:
                if sign == 'up':
                    sign = 'down'
                    i += 1
                elif sign == 'down':
                    i += 1
                else:
                    return False
            else:
                return False
        return True if sign == 'down' else False


if __name__ == '__main__':
    test = Solution()
    print(test.validMountainArray([2]))
