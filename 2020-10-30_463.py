class Solution:
    def islandPerimeter(self, grid) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res += 4
                    if j - 1 >= 0:
                        if grid[i][j - 1] == 1:
                            res -= 1
                    if j + 1 < len(grid[i]):
                        if grid[i][j + 1] == 1:
                            res -= 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            res -= 1
                    if i + 1 < len(grid):
                        if grid[i + 1][j] == 1:
                            res -= 1
                    print(res)
        return res


if __name__ == '__main__':
    test = Solution()
    lst = [[0, 1, 0, 0],
           [1, 1, 1, 0],
           [0, 1, 0, 0],
           [1, 1, 0, 0]]
    print(test.islandPerimeter(lst))
