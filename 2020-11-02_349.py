class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    def intersection_2(self, nums1, nums2):
        len_num1 = len(nums1)
        len_num2 = len(nums2)
        nums1.sort()
        nums2.sort()
        j = 0
        k = 0
        res = []
        while j < len_num1 and k < len_num2:
            if nums1[j] == nums2[k]:
                res.append(nums1[j])
                while j < len_num1 - 1:
                    if nums1[j + 1] == nums1[j]:
                        j += 1
                    else:
                        break
                while k < len(nums2) - 1:
                    if nums2[k + 1] == nums2[k]:
                        k += 1
                    else:
                        break
                j += 1
                k += 1
            elif nums1[j] < nums2[k]:
                while j < len_num1 - 1:
                    if nums1[j + 1] == nums1[j]:
                        j += 1
                    else:
                        break
                j += 1
            else:
                while k < len(nums2) - 1:
                    if nums2[k + 1] == nums2[k]:
                        k += 1
                    else:
                        break
                k += 1
        return res


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1, 12, 312, 3, 21, 32, 1]
    nums2 = [2, 2]
    test = Solution()
    print(test.intersection_2(nums1, nums2))
