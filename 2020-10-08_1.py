class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

     

    示例:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    """
    def twoSum(self, nums, target):
        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
        length = len(nums)
        left = 0
        right = length - 1
        ans = []
        nums.sort()
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                ans = [sorted_id[left], sorted_id[right]]
                break
        return ans

    def twoSum_2(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


if __name__ == '__main__':
    test = Solution()
    print(test.twoSum_2([2, 7, 11, 15], 9))
