class Solution:
    """
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

    注意:

    每个数组中的元素不会超过 100
    数组的大小不会超过 200
    示例 1:

    输入: [1, 5, 11, 5]

    输出: true

    解释: 数组可以分割成 [1, 5, 5] 和 [11].
     

    示例 2:

    输入: [1, 2, 3, 5]

    输出: false

    解释: 数组不能分割成两个元素和相等的子集.
    """
    def canPartition(self, nums) -> bool:
        """
        参考二叉树的dfs，遍历数组中的每一个节点，朝左朝右分别为选，不选
        如果从头结点到根节点的值相加等于数组值的一半，那么就存在两个数据的和相等
        """
        n = len(nums)
        if len(nums) < 2:
            return False
        if sum(nums) % 2 == 1:
            return False
        else:
            target = sum(nums) // 2
        if max(nums) > target:
            return False
        print(target)

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]


if __name__ == '__main__':
    test = Solution()
    print(test.canPartition([2, 2 ]))
