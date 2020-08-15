r"""
二叉树的中根遍历

两种方法

-   递归
-   借助stack迭代

递归不谈了。迭代法要讲讲，挺难的，而且面paypal的时候被问到了……

看了很多教程还是不明白，最后自己用模拟函数调用帧搞定了。要理解这种，先要理解所谓帧到底是啥。简而言之就是这是函数调用的第几层（老千层饼了），比如假如这是第一次调用f()，那么就是第0层，stack上面什么都没有。如果在第0层里又调用了一次f()，那么进入新的f()之后，就是第1层，此时stack上面有第0层暂存的现场，包括局部变量、返回地址，有点像游戏里检查点的感觉。只有这样，当从第1层返回到第0层的时候，第0层才能知道刚才自己做了啥、接下来应该从哪里开始执行。举个例子

::

    # 开始调用f()
    f() {
        # 这是第0层，此时stack是空的
        x = 1
        # 将要再次调用f()
        f() {
            # 这是第1层，此时stack里是[(x = 1, label)]
            x = 2
            # x变成了2
        }
        label: # 这是从第1层返回后，第0层继续执行的位置
        # 从第1层返回了，stack又空了，x又变成了1
    }

递归里面每一层都有可能会调用2次子函数，一次是遍历左边子树、另一次是遍历右边子树，所以我们只要标记3个检查点就可以了。

.. code-block:: python

    if root:
        # 这是第0个检查点，表示函数刚刚开始执行，啥也没做呢
        res = []
        if root.left:
            res += self.inorderTraversal(root.left)
        # 这是第1个检查点，表示左边子树已经遍历完了，将要遍历当前节点和右边子树
        res.append(root.val)
        if root.right:
            res += self.inorderTraversal(root.right)
        # 这是第2个检查点，表示所有的事情都做完了，等待返回
        return res
    else:
        return []

然后如果发现现在在检查点0，说明将要遍历左边子树，就先把当前节点、检查点1放到stack里，把当前节点设置成左边节点、检查点设置成0，这样就相当于给子函数传了参数，进入了子函数。

如果发现现在在检查点1，说明刚才已经遍历过左边子树了，现在应该要遍历当前节点了，就先遍历当前节点，然后如果发现又要遍历右边子树，那么还是把当前节点、检查点2放到stack里，然后把当前节点设置成右边节点、检查点设置成0。

如果发现现在在检查点2，说明所有的事情都做完了，直接pop stack，把当前节点、检查点设置成刚才pop的东西，这样相当于回到了上一层帧。

千言万语不如举个例子，比如

::

    1
     \
      2
     /
    3

这棵树。遍历过程是这样的

1.  当前节点1、检查点0、stack空
2.  （节点1）因为发现左边子树不存在，所以直接跳到检查点1
3.  （节点1）遍历节点1
4.  （节点1）发现右边子树存在，所以暂存当前帧，把当前节点（现在是1）、子函数返回后继续开始执行的检查点（是2）放到stack里，stack变成了 ``[(1, 2)]``
5.  （节点1）传入参数，调用子函数，当前节点变成2、检查点0、stack是 ``[(1, 2)]``
6.  （节点2）发现要遍历左边子树，所以暂存当前帧，把当前节点（现在是2）、子函数返回后继续执行的检查点（是1）放到stack里，stack变成了 ``[(1, 2), (2, 1)]``
7.  （节点2）传入参数，调用子函数，当前节点变成3、检查点0、stack是 ``[(1, 2)]``
8.  （节点3）节点3发现左边子树不存在，直接跳到检查点1
9.  （节点3）遍历节点3
10. （节点3）发现右边子树不存在，直接跳到检查点2
11. （节点3）发现在检查点2，所以返回上一层帧，所以pop stack，当前节点变成3、检查点1，stack是 ``[(1, 2)]``
12. （节点2）遍历节点2
13. （节点2）发现右边子树不存在，直接跳到检查点2
14. （节点2）发现在检查点2，所以返回上一层，pop stack，当前节点变成1、检查点2，stack是 ``[]``
15. （节点1）发现在检查点2，而现在已经在最顶层了，说明程序结束
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if root:
    #         res = []
    #         if root.left:
    #             res += self.inorderTraversal(root.left)
    #         res.append(root.val)
    #         if root.right:
    #             res += self.inorderTraversal(root.right)
    #         return res
    #     else:
    #         return []
    # 递归的太简单了

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     stack = []
    #     res = []
    #     head = root

    #     while not (head == None and len(stack) == 0):

    #         while head != None:
    #             stack.append(head)
    #             head = head.left

    #         head = stack.pop()
    #         res.append(head.val)
    #         head = head.right

    #     return res
    # 这太难理解了

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     stack = []
    #     res = []
    #     head = root

    #     while not (stack == [] and head == None):
    #         if head:
    #             stack.append(head)
    #             head = head.left
    #         else:
    #             head = stack.pop()
    #             res.append(head.val)
    #             head = head.right

    #     return res
    # 这也很难理解

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            stack = [] # 放上一层的节点、返回地址
            res = []
            head = root # 当前这帧在看哪个节点
            pc = 0 # 当前这帧跑到哪里了，类似程序计数器

            while True:
                if pc == 0: # 如果当前啥都没做，有可能我们是在子函数的最开头，啥也没开始做的时候
                    if head.left: # 如果有左边子树，那么要先遍历左边子树，所以需要暂存一下当前帧，存当前帧的节点和返回地址就可以了
                        pc = 1 # 从遍历左边子树的子函数返回之后，应该是回到1的位置开始执行
                        stack.append((head, pc)) # 保存当前帧
                        head = head.left # 传入参数
                        pc = 0 # 调用遍历左边子树的子函数
                    else: # 如果没有左边子树
                        pc = 1 # 那么直接跳到1的位置
                elif pc == 1: # 如果现在在1的位置，说明刚才已经遍历过左边子树了
                    res.append(head.val) # 现在应该遍历当前节点了
                    if head.right: # 如果有右边子树，就要遍历右边子树，同样暂存当前帧
                        pc = 2 # 从遍历右边子树的子函数返回之后，应该是回到2的位置开始执行
                        stack.append((head, pc)) # 保存当前帧
                        head = head.right # 传入参数
                        pc = 0 # 调用遍历右边子树的子函数
                    else: # 如果没有右边子树
                        pc = 3 # 就直接跳到3的位置
                else: # 如果现在在3的位置，说明所有的事情都搞定了，可以直接返回了
                    if stack: # 如果当前帧不是顶层帧
                        head, pc = stack.pop() # 返回到上一层
                    else: # 已经是最顶层帧了
                        break

            return res
        else:
            return []

root = TreeNode(1)
root.left = None
root.right = TreeNode(2)
root.right.left = TreeNode(3)
s = Solution()
print(s.inorderTraversal(root)) # [1, 3, 2]