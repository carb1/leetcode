class Solution:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。

    示例 1:

    输入: ["flower","flow","flight"]
    输出: "fl"
    示例 2:

    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
    """

    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        index = 0
        s = strs[0]
        status = False
        head = ''
        while index <= len(s) - 1:
            for i in strs:
                if index <= len(i) - 1:
                    if i[index] == s[index]:
                        status = True
                    else:
                        status = False
                        break
                else:
                    status = False
                    break
            if status:
                head += s[index]
                index += 1
            else:
                break
        return head

    def longestCommonPrefix_2(self, strs) -> str:
        if len(strs) == 0:
            return ''
        floor = min(strs)
        ceil = max(strs)
        for i in range(len(floor)):
            if floor[i] != ceil[i]:
                return floor[:i]
        return floor

    def longestCommonPrefix_3(self, strs) -> str:
        if len(strs) == 0:
            return ''
        s = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


if __name__ == '__main__':
    test = Solution()
    print(test.longestCommonPrefix_3(["flower", "flow", "flight"]))
