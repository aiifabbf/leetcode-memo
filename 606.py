# 先根遍历二叉树，然后构建一个带括号的字符串。

# 其实我没有很明白这个字符串里的括号到底是怎么回事……反正分四种情况就完事儿了。

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        # 总之先套先根遍历的模板好了
        if t:
            if t.left != None and t.right != None:
                return f"{t.val}({self.tree2str(t.left)})({self.tree2str(t.right)})"
            elif t.left != None and t.right == None:
                return f"{t.val}({self.tree2str(t.left)})"
            elif t.left == None and t.right != None:
                return f"{t.val}()({self.tree2str(t.right)})"
            else:
                return f"{t.val}"
        else:
            return ""