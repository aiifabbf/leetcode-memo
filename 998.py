"""
往一个maximum binary heap里插入一个节点。

做法很简单，先把val和root比较大小，如果比root的值还大，就自己造个新节点作为根节点、val作为根节点的值，然后把原树变成新节点的 **左边子树** ；如果比root的值小，就递归地往 **右边子树** 传播。

至于为什么一定是左边子树和右边子树，是因为题目里有个坑，不仔细读题是没法注意到的

    Suppose B is a copy of A with the value val appended to it. It is guaranteed that B has unique values.

意思是说，原树是用某个array构造的，而要你返回的新的树，是用原来的array最后追加val之后的新array构造出来的。所以可想而知，当val比root值还大的时候，val变成了根节点，val之前的substring构造出了左边子树，而val之后没有元素了，所以右边子树为空；当val比root值小的时候，val进的是root所在的位置的后半边substring，而后半边substring变成了右边子树，所以val要往右边子树传播。

还是照理画两个图。第一个是val比root值大的时候， ``[]`` 代表左边子树， ``o`` 代表根节点， ``()`` 代表右边子树

::

    [       ] o (       ) <- val

因为val比 ``o`` 还大，所以如果这时候构造maximum binary heap，val会变成根节点，前面的所有元素变成左边子树，整个树变成了

::

    [                   ] o

如果val比root值小

::

    [       ] o (       val)

此时构造maximum binary heap，左边子树、根节点的结构都不变，val变成了右边子树中的某一个节点，应该传播给右边子树处理。至于val到了右边子树里面怎么处理，就靠下一层递归了。

整个思路感觉还是挺顺的。

654题是从array构造一个maximum binary heap。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if val > root.val: # 比根节点还大
                node = TreeNode(val) # val变成根节点
                node.left = root # 原树变成根节点的左边子树
                return node
            else:
                # root.left = self.insertIntoMaxTree(root.left, val) # 这道题不能往左边子树插，而应该往右边子树插
                root.right = self.insertIntoMaxTree(root.right, val) # val变成了右边子树中的一个节点，val传播给右边子树处理
                return root
        else: # 空树
            return TreeNode(val) # 直接形成新节点，变成根节点