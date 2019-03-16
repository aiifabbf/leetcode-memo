# 判断一个二叉树是不是沿y轴对称

# 一开始的想法是把左边子树先invert一下（226题，著名的homebrew作者翻车题），再和右子树比较是不是完全一致（100题）。好像时间复杂度阶数是一样的啊……好像不用这么麻烦

# 好像广度优先、按层遍历更好写一点……好像也不是很好写，除非把所有的null都放进来

# 考虑这样一个思路，一个树关于y轴对称，等价于自己和自己镜面对称。两个树镜面对称的要求是

# -   根节点值相同
# -   树a的左边子树和树b的右边子树镜面对称
# -   树a的右边子树和树b的左边子树镜面对称

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# import copy
import functools
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    @functools.lru_cache()
    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None and t2 != None:
            return False
        elif t1 != None and t2 == None:
            return False
        elif t1 != None and t2 != None:
            return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
        else:
            return True