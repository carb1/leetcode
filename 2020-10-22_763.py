class Solution:
    """
    输入：S = "ababcbacadefegdehijhklij"
    输出：[9,7,8]
    解释：
    划分结果为 "ababcbaca", "defegde", "hijhklij"。
    每个字母最多出现在一个片段中。
    像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
    """
    def partitionLabels(self, S: str):
        if not S: return []
        dic = {s: index for index, s in enumerate(S)}  # 存储某个字母对应地最后一个序号
        num = 0  # 直接计数
        result = []
        j = dic[S[0]]  # 第一个字符的最后位置

        for i in range(len(S)):  # 逐个遍历
            num += 1  # 找到一个就加1个长度
            if dic[S[i]] > j:  # 思路一样，如果最后位置比刚才的大，就更新最后位置
                j = dic[S[i]]
            if i == j:  # 思路一样，形式不同，这里就是找到这一段的结束了，就说明当前位置的index和这个字母在字典里的最后位置应该是相同的。
                result.append(num)  # 加入result
                num = 0  # 归0
        return result

    def partitionLabels_2(self, S: str):
        if not S: return []
        hashmap = {}
        n = len(S)
        for i in range(n):
            if S[i] in hashmap:
                hashmap[S[i]].append(i)
            else:
                hashmap[S[i]] = [i]
        index_list = set()
        for i in hashmap:
            lst = hashmap[i]
            for i in hashmap:
                if hashmap[i][0] < max(lst):
                    lst += hashmap[i]
            index_list.add((min(lst), max(lst)))
        res_range = [0]
        for i in index_list:
            res_range.append(i[1] + 1)
        res_range.sort()
        print(res_range)
        res = []
        for i in range(len(res_range) - 1):
            res.append(res_range[i + 1] - res_range[i])
            # print(s[res_range[i]:res_range[i + 1]])
        return res

if __name__ == '__main__':
    test = Solution()
    print(test.partitionLabels("ababcbacadefegdehijhklij"))

