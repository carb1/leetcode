import math


class Solution:
    """
    给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

    进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

    示例 1：
    输入：nums1 = [1,3], nums2 = [2]
    输出：2.00000
    解释：合并数组 = [1,2,3] ，中位数 2

    示例 2：
    输入：nums1 = [1,2], nums2 = [3,4]
    输出：2.50000
    解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

    示例 3：
    输入：nums1 = [0,0], nums2 = [0,0]
    输出：0.00000

    示例 4：
    输入：nums1 = [], nums2 = [1]
    输出：1.00000

    示例 5：
    输入：nums1 = [2], nums2 = []
    输出：2.00000
    """

    def helper(self, nums1, nums2, k):
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        t = min(k // 2, len(nums2))
        if nums1[t - 1] > nums2[t - 1]:
            return self.helper(nums1, nums2[t:], k - t)
        else:
            return self.helper(nums1[t:], nums2, k - t)

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2
        return (self.helper(nums1, nums2, k1) + self.helper(nums1, nums2, k2)) / 2

    def findMedianSortedArrays_2(self, nums1, nums2) -> float:
        lst = nums1 + nums2
        lst.sort()
        length = len(lst)
        if length % 2 == 0:
            ans = ((lst[int(length / 2)] + lst[int(length / 2) - 1])) / 2
        else:
            ans = lst[int(length / 2)]
        return ans


if __name__ == '__main__':
    nums1 = [2, 7]
    nums2 = [3, 4, 7]
    test = Solution()
    print(test.findMedianSortedArrays(nums1, nums2))
    k1 = (len(nums1) + len(nums2) + 1) // 2
    k2 = (len(nums1) + len(nums2) + 2) // 2
    print(k1, k2)
