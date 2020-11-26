class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        n = len(nums) - 3
        res = []
        for i in range(n):
            pass



if __name__ == '__main__':
    test = Solution()
    print(test.fourSum([1, 0, -1, 0, -2, 2], 0))