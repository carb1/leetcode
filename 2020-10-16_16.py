class Solution:
    """
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

    示例：

    输入：nums = [-1,2,1,-4], target = 1
    输出：2
    解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
    """

    def threeSumClosest(self, nums, target: int) -> int:
        if len(nums) <= 3:
            return sum(nums)
        nums.sort()
        n = len(nums)
        res = float('inf')
        fan = 0
        for i in range(n):
            floor = i + 1
            ceil = n - 1
            while floor < ceil:
                d = nums[i] + nums[floor] + nums[ceil] - target
                if abs(d) < res:
                    res = min(res, abs(d))
                    fan = d + target
                if d < 0:
                    floor += 1
                elif d > 0:
                    ceil -= 1
                else:
                    return fan

        return fan


if __name__ == '__main__':
    test = Solution()
    print(test.threeSumClosest([0, 1, 1, 1], 100))
