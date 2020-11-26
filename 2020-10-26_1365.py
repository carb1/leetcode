class Solution:
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        res = []
        for i in range(n):
            count = 0
            for num in nums:
                if num < nums[i]:
                    count += 1
            res.append(count)
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.smallerNumbersThanCurrent([7,7,7,7]))
