class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = 0
        time = 0
        while time < n:
            if nums[index] == 0:
                nums.remove(0)
                nums.append(0)
                index -= 1
            time += 1
            index += 1
        return nums

    def moveZeroes_2(self, nums: list) -> None:
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if index == i:
                    index += 1
                else:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
        return nums



if __name__ == '__main__':
    test = Solution()
    print(test.moveZeroes_2([2, 1]))
