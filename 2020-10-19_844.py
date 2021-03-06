class Solution:
    """
    给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
    注意：如果对空文本输入退格字符，文本继续为空。

    示例 1：

    输入：S = "ab#c", T = "ad#c"
    输出：true
    解释：S 和 T 都会变成 “ac”。
    示例 2：

    输入：S = "ab##", T = "c#d#"
    输出：true
    解释：S 和 T 都会变成 “”。
    示例 3：

    输入：S = "a##c", T = "#a#c"
    输出：true
    解释：S 和 T 都会变成 “c”。
    示例 4：

    输入：S = "a#c", T = "b"
    输出：false
    解释：S 会变成 “c”，但 T 仍然是 “b”。
    """
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = list(S)
        t = list(T)
        s_new = []
        t_new = []
        for i in s:
            if i == '#':
                if len(s_new) > 0:
                    s_new.pop()
                else:
                    continue
            else:
                s_new.append(i)
        for i in t:
            if i == '#':
                if len(t_new) > 0:
                    t_new.pop()
                else:
                    continue
            else:
                t_new.append(i)
        return ''.join(s_new) == ''.join(t_new)


if __name__ == '__main__':
    test = Solution()
    print(test.backspaceCompare("ab#c", "ad#c"))
