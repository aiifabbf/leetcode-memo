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
-   958 判断二叉树是不是完全二叉树
-   662 二叉树的最大宽度
-   449 序列化、反序列化二叉树的方法
-   406
-   898
-   863
-   1015

可优化
==========

-   523 找substring能否累加得到k的整数倍
-   653 二分搜索树中的two sum
-   671 找到一个满足一些特殊性质的二叉树里的倒数第二小的节点值
-   543 二叉树里任意两点之间的距离的最大值
-   235 在二分搜索树里找到两个节点的最近公共祖先节点
-   222 数出一个完全二叉树里的节点个数
-   88  合并两个从小到大排好序的array

一些模板
==========

判断一个array是不是另一个array的subsequence（可以不连续）
--------------------------------------------------

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

判断一个array是不是另一个array的substring（连续）
-------------------------------------------

.. code:: python


二叉树的先根遍历
-------------

可以用递归

.. code:: python

    # 改编自144

    class Solution:
        def preorderTraversal(self, root: TreeNode) -> List[int]:
            if root:
                doSomthing(root.val) # 比如放入数组之类的
                if root.left:
                    self.preorderTraversal(root.left)
                if root.right:
                    self.preorderTraversal(root.right)
            else:
                pass

也可以用迭代、借助stack。好处有两个

-   速度快一点
-   不受递归深度限制

.. code:: python

    # 改编自144

    class Solution:
        def preorderTraversal(self, root: TreeNode) -> List[int]:
            if root:
                res = []
                stack = [root]

                while stack:
                    node = stack.pop()
                    res.append(node.val) # 这里相当于访问node
                    if node.right: # 这里要记住是右边先进stack
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)

                return res
            else:
                return []

.. note:: 先根遍历路径的特点

    先根遍历路径的第一个元素永远是根节点，然后接下来是左边子树、右边子树。图像类似这样

    ::

        o [     ] (     )
        ------------------
        0 1     ? ?      n

    所以除了能确定第一个元素是根节点，其他的信息比如

    -   第二个元素开始是属于左边子树还是右边子树？
    -   从第几个元素开始是左边子树和右边子树的边界？
    -   ...

    都是不知道的。

二叉树的中根遍历
-------------

可以用递归，只要把对根节点的访问的语句放到中间就算中根遍历了。

.. code:: python

    # 改编自94

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

也可以借助stack，然后迭代，但是写起来挺麻烦的……

.. note::

    二分搜索树（BST）用中根遍历之后，会得到排好序的array。

.. note:: 中根遍历路径的特点

    中根遍历路径的第一个元素可能是左边子树、也可能是根节点（如果左边子树不存在的话）。图像类似这样

    ::

        [       ] o (       )
        ---------------------
        0         ? ?        n

    所以单靠中根遍历路径其实不能得到什么有用的信息。

    但是如果中根遍历路径和先根遍历路径同时给出（105题）、或者中根遍历路径和后根遍历路径同时给出（106题），就可以还原出树本来的结构。

    以中根遍历路径和先根遍历路径为例，

    1.  中根遍历路径的第一个元素肯定是根节点的值。
    2.  在先根遍历路径里找到根节点的值的位置，这样就能知道

        -   在这之前的所有元素都是属于左边子树的，且左边子树的节点个数也是知道的。
        -   在这之后的所有元素都是属于右边子树的，且右边子树的节点个数也是知道的。

        再回到中根遍历路径里，因为左边子树的节点个数知道了（假设是n），所以中根遍历路径里从第2个元素到第2 + n - 1个元素是属于左边子树的，从第2 + n个元素一直到最后都是属于右边子树的。

    3.  递归地把左边子树、右边子树的结构按同样的方法恢复出来。

衍生

-   105 从中根、先根遍历路径中恢复出二叉树
-   106 从中根、后根遍历路径中恢复出二叉树
-   889 从先根、后根遍历路径中恢复出二叉树的一种可能

二叉树的后根遍历
-------------

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
                    i = queue.pop(0)
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

.. note:: 如果一个二叉树是 完全二叉树_ 的话，那么对这个完全二叉树的广度优先遍历有一个性质：如果遇到一个节点是null，那么以后就不再会遇到非null节点。

    而且这条性质是充分必要的，如果一个树不是完全二叉树，那么它不会满足这条性质；如果一个树是完全二叉树，那么它一定满足这条性质。

    958题里我利用了这条性质。

.. _完全二叉树: https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees

衍生

-   103 二叉树的zigzag遍历
-   513 二叉树最后一层的最左边节点的值
-   515 二叉树最后一层的最大节点值

得到二叉树的深度
-------------

以前一直是用广度优先、按层遍历来做的（104题），但是也有非常简单的写法，比如

.. code:: python

    # 摘自543

    class Solution:
        def maxDepth(self, root: TreeNode) -> int:
            if root:
                return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            else:
                return 0

不一定比按层遍历快，但是写起来足够简单。

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
-   988
-   113

判断二叉树是不是二分搜索树（BST）
----------------------------

.. code:: python

    # 摘自98

    class Solution:
        def isValidBST(self, root: TreeNode) -> bool:
            return self.isBST(root, float("-inf"), float("inf"))

        def isBST(self, root: TreeNode, lower: int, upper: int) -> bool: # 除了root还要传入上下界
            if root:
                if root.val > lower and root.val < upper: # 首先根节点要在上下界之内
                    if root.left != None and root.right == None: # 左边子树非空、右边子树空
                        return root.left.val < root.val and self.isBST(root.left, lower, root.val) # 下界不变，上界变成根节点的值
                    elif root.left == None and root.right != None: # 左边子树空、右边子树非空
                        return root.right.val > root.val and self.isBST(root.right, root.val, upper) # 下界变成根节点的值，上界不变
                    elif root.left != None and root.right != None:
                        return root.left.val < root.val and root.right.val > root.val and self.isBST(root.left, lower, root.val) and self.isBST(root.right, root.val, upper)
                    else:
                        return True
                else: # 不然即使自己是BST，作为子树放在上层里也不能使大树是BST
                    return False
            else: # 空树是BST
                return True

排好序的array转换到height-balanced BST
------------------------------------

.. code:: python

    # 摘自108

    class Solution:
        def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
            if len(nums) == 0: # 空树
                return None
            elif len(nums) == 1: # 数组只含一个元素
                return TreeNode(nums[0])
            else: # 数组含有2个及以上的元素，这时候可以继续拆
                n = len(nums)
                root = TreeNode(nums[n // 2]) # 取最中间一个元素作为根节点
                root.left = self.sortedArrayToBST(nums[0: n // 2]) # 构造左边子树
                root.right = self.sortedArrayToBST(nums[n // 2 + 1:]) # 构造右边子树
                return root

衍生

-   1008 从二分搜索树的先根遍历路径重建出二分搜索树

筛选出出现频次最高的元素
--------------------

提示一下，如果有多种元素出现的频次一样而且恰好最高，怎么写最好？

.. code:: python

    # 摘自 https://leetcode.com/problems/most-frequent-subtree-sum/discuss/98675/Python-easy-understand-solution

    maximumFrequency = max(counter.values()) # 首先得到最高频次
    return [i for i, v in counter.items() if v == maximumFrequency] # 再筛选出频次和最高频次一样大的元素

计算器
-----