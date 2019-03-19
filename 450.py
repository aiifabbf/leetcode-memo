"""
从一个二分搜索树里删除一个节点。注意不是删完就完事儿了，删完还要保证剩下的节点构成一个二分搜索树。

最暴力的做法是中根遍历，得到从小到大排好序的array，然后删掉元素，再从这个array重现构造出二分搜索树。复杂度应该是 :math:`O(n)` ，因为要遍历每个节点。但是题目要求复杂度是 :math:`O(\log n)` 。

如果定位到了要删除的那个节点，会出现三种可能的情况

-   这个节点是叶子

    最简单的情况，直接删掉就好了。

-   这个节点左边子树存在，右边子树不存在

    删掉节点，把左边子树整个移过来。

-   这个节点左边子树不存在，右边子树存在

    同理。

-   这个节点左边子树、右边子树都存在

    这是最复杂的情况。需要 [#]_

    1.  把本节点的值修改成 **右边子树里的最小值**

        二分搜索树的中根遍历路径是一个从小到大排好序的array，所以直接给右边子树做中根遍历，路径的第一个元素就是右边子树里的最小值。

    2.  删掉右边子树里最小值所在的节点

        可以复用前面的过程。

.. [#] https://en.wikipedia.org/wiki/Binary_search_tree#Deletion
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else: # 定位到节点了
                if root.left == None and root.right == None: # 叶子
                    return None # 直接删掉
                elif root.left != None and root.right == None: # 只存在左边子树
                    return root.left # 左边子树整个移过来
                elif root.left == None and root.right != None: # 只存在右边子树
                    return root.right # 右边子树整个移过来
                else: # 最复杂的情况，两边子树都存在
                    root.val = self.inorderTraversal(root.right)[0] # 把本节点的值替换成右边子树里的最小值
                    root.right = self.deleteNode(root.right, root.val) # 再删掉右边子树里的最小值所在的节点
            return root
        else:
            return None

    def inorderTraversal(self, root: TreeNode) -> List[int]: # 还记得二分搜索树的中根遍历路径是从小到大排好序的array吗？
        if root:
            res = []
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
            return res
        else:
            return []