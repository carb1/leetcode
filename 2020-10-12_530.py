# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

 

    示例：

    输入：

       1
        \
         3
        /
       2

    输出：
    1

    解释：
    最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
     

    提示：

    树中至少有 2 个节点
    """
    def getMinimumDifference(self, root) -> int:
        def dfs(root):
            nonlocal pre, res
            if not root:
                return
            dfs(root.left)
            if pre != -1:
                res = min(res, root.val - pre)
            pre = root.val
            dfs(root.right)

        pre = -1
        res = float('inf')
        dfs(root)
        return int(res)

    def getMinimumDifference_2(self, root) -> int:
        stack = []
        res = float('inf')
        pre = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                t = stack.pop()
                if pre:
                    res = min(res, t.val - pre.val)
                pre = t
                root = t.right
        print(res)
        return res


if __name__ == '__main__':
    lst = [1, 2, 3]
    a = lst.pop()
    print(a)
    print(lst)
