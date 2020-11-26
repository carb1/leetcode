class Solution:
    """
    给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

     

    示例 1：

    输入：[-4,-1,0,3,10]
    输出：[0,1,9,16,100]
    示例 2：

    输入：[-7,-3,2,3,11]
    输出：[4,9,9,49,121]
    """

    def sortedSquares(self, A):
        return sorted([i * i for i in A])

    def sortedSquares_2(self, A):
        lst = []
        floor, ceil = 0, len(A) - 1
        while floor <= ceil:
            if abs(A[floor]) > abs(A[ceil]):
                lst.insert(0, A[floor] ** 2)
                floor += 1
            else:
                lst.insert(0, A[ceil] ** 2)
                ceil -= 1
        return lst


if __name__ == '__main__':
    test = Solution()
    print(test.sortedSquares([-7, -3, 2, 3, 11]))
