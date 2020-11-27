#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
import collections


class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        ans = 0
        count = collections.Counter(u + v for u in A for v in B)
        print(count)
        for i in C:
            for j in D:
                if -i - j in count:
                    ans += count[-i - j]
        return ans


# @lc code=end
if __name__ == '__main__':
    test = Solution()
    print(test.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
