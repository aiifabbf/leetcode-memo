=============
leetcode备忘录
=============

.. note:: 前情提要

    前大概200题在我\ 博客_\ 上。

    二刷的时候都会整理到这里来。

.. _博客: http://aiifabbf.github.io/leetcode中的算法

.. contents::

未解决
==========

-   743
-   713
-   475
-   784
-   399 
-   866 找不小于n的最小回文素数
-   491 找数组的递增subsequence
-   223 找出两个矩形的相交区域的面积
-   805 拆数组，拆成两个平均值相同的数组
-   835 平移找矩阵最大重合面积
-   994 元胞自动机
-   436 寻找区间列里比现在这个大的最小的区间
-   98 检查一个树是不是二分搜索树
-   543 二叉树里任意两点之间的距离的最大值
-   958 判断二叉树是不是完全二叉树
-   101 判断二叉树是不是沿y轴对称

可优化
==========

-   523 找substring能否累加得到k的整数倍

一些模板
==========

判断一个array是不是另一个array的subsequence（可以不连续）
------------------------------------------------

.. code:: python

    def isSubArray(subarray, array):
        pos = -1
        for i in subarray:
            try:
                pos = array.index(i, start=pos + 1)
            except:
                return False
        else:
            return True

二叉树的先根遍历
----------

.. code:: python

    # 改编自144

    class Solution:
        def preorderTraversal(self, root: TreeNode) -> List[int]:
            if root:
                doSomthing(root.val)
                if root.left:
                    self.preorderTraversal(root.left)
                if root.right:
                    self.preorderTraversal(root.right)
            else:
                pass

二叉树的中根遍历
----------

.. code:: python

    class Solution:
        def inorderTraversal(self, root: TreeNode) -> List[int]:
            if root:
                if root.left:
                    self.inorderTraversal(root.left)
                doSomthing(root.val)
                if root.right:
                    self.inorderTraversal(root.right)
            else:
                pass

二叉树的后根遍历
----------

.. code:: python

    class Solution:
        def postorderTraversal(self, root: TreeNode) -> List[int]:
            if root:
                if root.left:
                    self.postorderTraversal(root.left)
                if root.right:
                    self.postorderTraversal(root.right)
                doSomthing(root.val)
            else:
                pass

树的广度优先遍历
-------------

.. code:: python

    class Solution:
        def levelOrder(self, root: 'Node') -> None:
            if root:
                queue = [root]
                while queue:
                    element = queue.pop(0)
                    doSomething(element)
                    queue += element.children
            else:
                pass

.. note:: 树的广度优先、按层遍历
    :name: 树的广度优先、按层遍历

    如果想一层一层遍历，可以不要直接把下一层的所有children都放到queue里，而是暂时先放到一个临时queue里面，等这一层完了，再把临时queue整个替换掉全局的那个queue。比如下面这个例子

    .. code:: python

        class Solution:
            def maxDepth(self, root: 'Node') -> int:
                if root:
                    depth = 1
                    queue = [root]
                    while queue:
                        levelQueue = sum((i.children for i in queue), [])
                        queue = levelQueue
                        depth += 1
                    return depth - 1
                else:
                    return 0

二叉树的广度优先遍历
-----------------

.. code:: python

    class Solution:
        def maxDepth(self, root: TreeNode) -> int:
            if root:
                queue = [root]
                while queue:
                    for i in queue:
                        if i.left:
                            queue.append(i.left)
                        if i.right: # 切记切记这里不是elif，是if，因为左边和右边根本没关系
                            queue.append(i.right)
                        doSomething(i)
            else:
                pass

.. note:: 二叉树的广度优先、按层遍历

    如果想一层一层遍历，和 `树的广度优先、按层遍历`_ 一样。

    .. code:: python

        class Solution:
            def maxDepth(self, root: TreeNode) -> int:
                if root:
                    depth = 1
                    queue = [root]
                    while queue:
                        levelQueue = []
                        for i in queue:
                            if i.left:
                                levelQueue.append(i.left)
                            if i.right: # 切记切记这里不是elif，是if，因为左边和右边根本没关系
                                levelQueue.append(i.right)
                        depth += 1
                        queue = levelQueue
                    return depth
                else:
                    return 0

取得二叉树的所有叶子节点值
----------------------

.. code:: python

    # 摘自872

    class Solution:
        def getLeaves(self, root: TreeNode) -> List[int]:
            if root:
                if root.left == None and root.right == None:
                    return [root.val]
                res = []
                if root.left:
                    res += self.getLeaves(root.left)
                if root.right:
                    res += self.getLeaves(root.right)
                return res
            else:
                return []

取得二叉树里根节点到所有叶子的路径
----------------------------

还是一个递归的思路。

一个二叉树根节点到所有叶子的路径，等于

-   左边子二叉树里根节点到所有叶子的路径
-   右边子二叉树里根节点到所有叶子的路径

加上根节点到左边子节点、根节点到右边子节点的两条路。

.. code:: python

    # 摘自257

    class Solution:
        def binaryTreePaths(self, root: TreeNode) -> List[str]:
            if root:
                if root.left == None and root.right == None: # 叶子
                    return [f"{root.val}"]
                elif root.left != None and root.right == None:
                    return [f"{root.val}->{i}" for i in self.binaryTreePaths(root.left)] # 根节点出发到左边子节点、加上左边子二叉树里根节点到所有叶子的路径
                elif root.left == None and root.right != None:
                    return [f"{root.val}->{i}" for i in self.binaryTreePaths(root.right)] # 根节点出发到右边子节点、加上右边子二叉树里根节点到所有叶子的路径
                else:
                    return [f"{root.val}->{i}" for i in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)] # 左右都加
            else: # 空节点
                return [] # 无路可走

衍生

-   129

计算器
-----

