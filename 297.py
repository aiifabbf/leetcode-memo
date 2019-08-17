"""
想一个序列化、反序列化二叉树的方法

看到题就想到可以用preorder和inorder唯一确定一个没有重复节点值的二叉树，可是题目里面没有说二叉树里会不会存在两个节点的值相同的情况，所以就没有用这种方法。

想到用嵌套list来表示二叉树，有点递归定义的感觉

-   list的第一个元素是节点值
-   第二个元素是另一个list，表示左边子树
-   第三个元素是另一个list，表示右边子树
-   空树用空list表示

::

    [root.val, [...], [...]]
                      ^---^----右边子树
               ^---^-----------左边子树
        ^----------------------节点值

变成list之后，再变成json string。这就完成了序列化。

反序列化的话，就先解析json string，变成嵌套list，然后再递归解包就好了。

两个问题

-   面试里可能会问到不准用json包怎么办，那好像又是编译原理的事情了……
-   其他语言可能不支持嵌套list
"""

from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import json

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return json.dumps(self.treeToList(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.listToTree(json.loads(data))

    def treeToList(self, root: TreeNode) -> List: # TreeNode表示的树变成嵌套list表示的树
        if root: # 不是空树
            tree = [root.val] # 第一个元素是节点的值
            tree.append(self.treeToList(root.left)) # 第二个元素是左边子树
            tree.append(self.treeToList(root.right)) # 第三个元素是右边子树
            return tree
        else: # 空树
            return []

    def listToTree(self, tree: List) -> TreeNode: # 嵌套list表示的树变成TreeNode表示的数
        if tree: # 不是空树
            root = TreeNode(tree[0]) # 第一个元素是节点的值，所以创建一个节点
            leftTree = self.listToTree(tree[1]) # 第二个元素是左边子树，所以递归地解出左边子树
            rightTree = self.listToTree(tree[2]) # 第三个元素是右边子树，所以递归地解出右边子树
            root.left = leftTree # 组装起来
            root.right = rightTree
            return root
        else: # 空树
            return None

    # 本来想用preorder和inorder来唯一确定一个二叉树的，但是突然发现题目里没有说二叉树里的节点值会不会重复，万一有重复，那就没法这么做了
    # def preorderTravesal(self, root: TreeNode) -> List[int]:
    #     if root:
    #         return [root.val] + self.preorderTravesal(root.left) + self.preorderTravesal(root.right)
    #     else:
    #         return []

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if root:
    #         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    #     else:
    #         return []

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))