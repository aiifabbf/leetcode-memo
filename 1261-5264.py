"""
给一棵树，做两件事情

-   根节点设置成0，然后对于树中的每个节点，它的左边子节点的值等于自身的值乘以二再加一，右边子节点的值等于自身的值乘以二加二
-   提供一个方法，判断一个值是否在树里

第一件事情直接用递归就好了。

第二件事情也很简单，在做第一件事情的同时，把每个节点值放到一个集合里面，这样下次就可以快速判断一个值是否在树里了。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        if root:
            root.val = 0

        self.seen = set() # 把树里出现的值统统放在集合里

        def recover(root: TreeNode): # 第一件事情，重建树
            if root:
                self.seen.add(root.val)
                if root.left:
                    root.left.val = 2 * root.val + 1 # 左边节点的值是当前节点值乘以二加一
                    recover(root.left) # 递归地重建左边子树
                if root.right:
                    root.right.val = 2 * root.val + 2 # 右边节点值是当前节点值乘以二加二
                    recover(root.right) # 递归地重建右边子树
            else:
                return

        recover(root)

    def find(self, target: int) -> bool: # 判断某个值是否在树里
        return target in self.seen # 有了集合就非常简单了，虽然费点内存，但是快啊


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)