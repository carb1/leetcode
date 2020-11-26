class Solution:
    """
    给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

    如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

     

    示例 1：

    输入：arr = [1,2,2,1,1,3]
    输出：true
    解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
    示例 2：

    输入：arr = [1,2]
    输出：false
    示例 3：

    输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
    输出：true
    """
    def uniqueOccurrences(self, arr) -> bool:
        dic = dict()
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        lst = []
        for j in dic:
            lst.append(dic[j])
        return len(lst) == len(set(lst))

    def uniqueOccurrences_2(self, arr):
        arr.sort()
        n = len(arr) - 1
        index = 0
        lst = []
        while index <= n:
            count = 1
            if index < n:
                while arr[index + 1] == arr[index]:
                    count += 1
                    index += 1
                    if index >= n:
                        break
            if count in lst:
                return False
            lst.append(count)
            index += 1
        return True


if __name__ == '__main__':
    test = Solution()
    print(test.uniqueOccurrences_2([-4, 3, 3]))
