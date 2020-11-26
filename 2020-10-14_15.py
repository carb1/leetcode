class Solution:
    """
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

     

    示例：

    给定数组 nums = [-1, 0, 1, 2, -1, -4]，

    满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    """

    def threeSum(self, nums):
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        n = len((nums))
        for i in range(n):
            if nums[i] > 0:
                return res
            if (nums[i] == nums[i - 1] and i > 0):
                continue
            floor = i + 1
            ceil = n - 1
            while floor < ceil:
                if (nums[i] + nums[floor] + nums[ceil] == 0):
                    res.append([nums[i], nums[floor], nums[ceil]])
                    while (floor < ceil and nums[floor] == nums[floor + 1]):
                        floor += 1
                    while (floor < ceil and nums[ceil] == nums[ceil - 1]):
                        ceil -= 1
                    floor += 1
                    ceil -= 1
                else:
                    if (nums[i] + nums[floor] + nums[ceil] > 0):
                        ceil -= 1
                    else:
                        floor += 1
        return res
