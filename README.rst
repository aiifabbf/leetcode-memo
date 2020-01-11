=============
leetcode备忘录
=============

.. default-role:: math

.. note:: 前情提要

    前大概200题在我\ 博客_\ 上。

    二刷的时候都会整理到这里来。

.. _博客: http://aiifabbf.github.io/leetcode中的算法

.. contents::

.. note:: 有些题号是 ``1024-5019`` 这种形式的，前一个数字表示题库里的编号，后一个数字表示contest里的编号。

    为什么从1010才开始这种题号形式呢？因为我从1013才开始做每周contest的，1010是我做virtual contest练手的。

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
-   449 序列化、反序列化二叉树的方法
-   406
-   898
-   863
-   1015
-   526 1到N满足某种性质的排列有多少种
-   805 把array分成两个平均值相同的subsequence
-   516 最长回文subsequence的长度
-   813 一个array最多分成k个substring，这些substring的平均值之和的最大值
-   845 最长山型substring
-   992 所有含有K种元素的substring的数量
-   817 链表里有多少个聚类
-   725 尽可能均匀地把链表分成K组
-   316 删掉重复的字符并且保证剩下的字符串的字典排序值最小
-   1031 存在路径能走到地图边缘的格子数量
-   315 找到当前元素前面比当前元素小的元素的个数
-   862 和大于等于K的substring的最小长度

可优化
==========

-   523 找substring能否累加得到k的整数倍
-   653 二分搜索树中的two sum
-   671 找到一个满足一些特殊性质的二叉树里的倒数第二小的节点值
-   543 二叉树里任意两点之间的距离的最大值
-   235 在二分搜索树里找到两个节点的最近公共祖先节点
-   222 数出一个完全二叉树里的节点个数
-   88  合并两个从小到大排好序的array
-   60  1-n的第k种组合
-   496 找原array里本元素位置右边开始的第一个比本元素大的元素值
-   1029    在没有bigint的情况下判断一个二进制数能否被5整除
-   24/25   不转换成list的前提下两两交换链表中相邻的两个节点位置
-   23  合并K个排好序的链表
-   430 在不先转换成list的前提下展平一个带分支的双向链表
-   55  能否跳到array的最后一格
-   44  针对wildcard优化

一些思路
==========

array中的目标函数优化问题
----------------------

一般形式是找到array中关于两个下标i, j的目标函数的最大值。

.. math::

    \max\{f(i, j) | 0 \leq i \leq n - 1, 0 \leq j \leq n - 1\}

实际问题中，i, j的取值可能有几种约束

-   :math:`i \neq j`
-   :math:`i < j`

:math:`f(i, j)` 可能有几种性质

-   与i, j的顺序无关，i, j可交换位置，即 :math:`f(i, j) = f(j, i)`
-   可以分解成关于i、关于j的两个独立函数，即 :math:`f(i, j) = u(i) + v(j)`

    .. note:: 比如1021题中， :math:`f(i, j) = f_1(i) + f_2(j)` 其中 :math:`f_1(i) = a_i + i, f_2(j) = a_j - j` 。

暴力搜索所有的情况的复杂度是 :math:`O(n^2)` 。

例

-   1014 一个中规中矩的dp题
-   1131 `f(i, j)` 是一个含有三对绝对值号的函数

array中满足某个条件的所有substring问题
-----------------------------------

一般形式是找到array中所有满足某个条件 :math:`g(i, j)` 的substring（要连续）。可能是个数，可能是具体的哪些 :math:`(i, j)` 。具体形式是求集合

.. math::

    \{(i, j) | g(i, j) = \text{True}, 0 \leq i \leq j \leq n - 1\}

一些模板
==========

判断一个array是不是另一个array的subsequence（可以不连续）
--------------------------------------------------

.. code-block:: python

    def isSubArray(subarray, array):
        pos = -1

        for v in subarray:
            try:
                pos = array.index(v, pos + 1) # .index()的start参数不是keyword...
            except:
                return False
        else:
            return True

判断一个array是不是另一个array的substring（连续）
-------------------------------------------

.. note:: 原来的代码

    .. code-block:: python

        def isSubString(substring, array):
            try:
                pos = array.index(substring[0]) # 找到第一个元素的起始位置
            except:
                return False

            for i in range(len(substring)):
                try: # 因为pos + i有可能越界，所以套个try
                    if substring[i] == array[pos + i]:
                        continue
                    else:
                        return False
                except:
                    return False

    其实是错的，试试 ``isSubstring("aaab", "aaaab")`` 还有 ``isSubstring("abaab", "aab")`` 。错误之处在于它只会从string里第一次出现 ``substring[0]`` 的地方开始找，如果发现不匹配，就不会往下找了，会直接返回 ``False`` 。

.. note:: 当然万能的Python可以一行搞定array是 ``str`` 时候的情况

    .. code-block:: python

        substring in array

    就搞定。


二叉树的先根遍历
-------------

可以用递归

.. code-block:: python

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

.. code-block:: python

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

.. code-block:: python

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
-   1028 从一种奇怪的先根遍历路径中恢复出二叉树

二叉树的后根遍历
-------------

.. code-block:: python

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

.. code-block:: python

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

    .. code-block:: python

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

.. code-block:: python

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

    .. code-block:: python

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

    用 ``levelQueue`` 其实有点浪费的，有更高效的写法，可以重复利用同一个queue，而不是每到下一层就建个新queue。说来也非常简单（但我怎么就没想到呢），记录一下queue一开始的长度就可以了

    .. code-block:: python

        class Solution:
            def maxDepth(self, root: TreeNode) -> int:
                if root:
                    depth = 0
                    queue = [root]

                    while queue:
                        # queue就代表第depth层上的所有节点了
                        length = len(queue)

                        for i in range(0, length):
                            v = queue.pop(0)
                            if v.left:
                                queue.append(v.left)
                            if v.right:
                                queue.append(v.right)

                        depth += 1
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
-   919 给完全二叉树插入节点
-   1161 二叉树每一层的和

得到二叉树的深度
-------------

以前一直是用广度优先、按层遍历来做的（104题），但是也有非常简单的写法，比如

.. code-block:: python

    # 摘自104

    class Solution:
        def maxDepth(self, root: TreeNode) -> int:
            if root:
                return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            else:
                return 0

不一定比按层遍历快，但是写起来足够简单。

如果用按层遍历来写，是

.. code-block:: python

    class Solution:
        def maxDepth(self, root: TreeNode) -> int:
            if root:
                depth = 0
                queue = collections.deque([root])

                while queue:
                    size = len(queue)

                    for _ in range(0, size):
                        v = queue.popleft()
                        if v.left:
                            queue.append(v.left)
                        if v.right:
                            queue.append(v.right)

                    depth += 1

                return depth
            else:
                return 0

取得二叉树的所有叶子节点值
----------------------

.. code-block:: python

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

.. code-block:: python

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

.. code-block:: python

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

.. code-block:: python

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

.. code-block:: python

    # 摘自 https://leetcode.com/problems/most-frequent-subtree-sum/discuss/98675/Python-easy-understand-solution

    maximumFrequency = max(counter.values()) # 首先得到最高频次
    return [k for k, v in counter.items() if v == maximumFrequency] # 再筛选出频次和最高频次一样大的元素

计算器
-----

允许元素重复、不允许组合重复
------------------------

意思是允许 ``[2, 2, 3]`` ，但是认为 ``[2, 2, 3], [3, 2, 2]`` 是重复的组合。

做法是先排个序，然后变成tuple，然后用set套一套，再变成list。

.. code-block:: python

    # 摘自39

    list(map(list, set(map(tuple, map(sorted, routes)))))

上面的代码可以做这种过滤。

找一个元素后面第一个比自己大的元素
-----------------------------

暴力做法是搜索，复杂度 :math:`O(n^2)` 。用stack可以做到 :math:`O(n)`

.. code-block:: python

    # 摘自739

    class Solution:
        def dailyTemperatures(self, T: List[int]) -> List[int]:
            # stack = [
            #     (0, T[0])
            # ]
            stack = [] # stack里的元素保证从底到顶递减（不是严格递减，可以相等）
            res = [0] * len(T) # 先初始化，每天都假设永远等不到气温比今天高的那天，这样最后不用补0什么的，方便一点

            for i, v in enumerate(T):
                if stack:

                    while True:
                        if stack:
                            day = stack.pop() # 这里pop了，后面如果发现大于等于今天的气温，记得要放回去
                            if v > day[1]: # 和stack顶部的元素比较，如果今天气温大于这一天的气温，说明那一天找到了离自己最近的、比自己气温高的那一天
                                res[day[0]] = i - day[0] # 把那一天的值设为今天和那一天的日期之差
                            else: # 发现今天气温小于等于那一天的气温，那么说明那一天至今都没有找到比自己气温高的日子，同时因为stack保证气温递减，所以顶部以下的日子都不用看了，能保证顶部以下的所有日子的气温都大于等于顶部那天的气温。
                                stack.append(day) # 记得把那一天放回去
                                stack.append((i, v)) # 再把今天放进去
                                break # 继续明天
                        else: # stack已经空了，没日子好比较了
                            stack.append((i, v)) # 直接把今天放进去
                            break # 继续明天

                else: # stack空的话，就直接放进去
                    stack.append((i, v))
            return res # 初始化的好处就是最后直接返回，不用补零什么的

遍历链表
----------

.. code-block:: python

    # 改编自206

    class Solution:
        def reverseList(self, head: ListNode) -> ListNode:
            if head:
                sentinel = head

                while head:
                    doSomething(head)
                    head = head.next

                return sentinel
            else:
                return None

.. note:: 颠倒链表（206题）

    .. code-block:: python

        class Solution:
            def reverseList(self, head: ListNode) -> ListNode:
                # return self.listToLinkedList(self.linkedListToList(head)[:: -1])
                if head:
                    sentinel = None

                    while head:
                        tempSentinel = ListNode(head.val)
                        tempSentinel.next = sentinel
                        sentinel = tempSentinel
                        head = head.next

                    return sentinel
                else:
                    return None

.. note:: 链表变成array

    可以看做遍历链表的过程。

    .. code-block:: python

        # 摘自206

        class Solution:
            def linkedListToList(self, head: ListNode) -> List:
                if head:
                    res = []

                    while head:
                        res.append(head.val)
                        head = head.next

                    return res
                else:
                    return []

.. note:: 遍历的同时不丢失之前一个节点

    在有些需求中，比如在删除第i个节点的时候，需要把第i-1个节点的next直接指向第i+1个节点，但是在遍历到第i个节点时候，如果用上面的代码会发现没办法再去找第i-1个节点了，第i-1个节点已经丢失了。

    此时就要用到假节点，然后再用一个previous记录head之前一个节点。

    .. code-block:: python

        # 摘自707

        class Solution:
            def deleteAtIndex(self, index: int) -> None: # 删除第i个节点
                """
                Delete the index-th node in the linked list, if the index is valid.
                """
                head = self.sentinel.next
                previous = self.sentinel
                i = 0

                while head:
                    if i == index: # 此时head是第i个节点，previous是第i-1个节点
                        previous.next = head.next # 直接跨过第i个节点，把第i-1个节点和后面的第i+1个节点连起来。
                        return
                    else:
                        i += 1
                        previous = head
                        head = head.next

array变成链表
-------------

.. code-block:: python

    # 摘自206

    class Solution:
        def listToLinkedList(self, array: List) -> ListNode:
            if array:
                head = ListNode(0) # 先生成一个假节点
                sentinel = head # 不要丢了假节点的引用

                for v in array:
                    head.next = ListNode(v)
                    head = head.next

                return sentinel.next # 第一个是假节点，没用，返回假节点后面的第一个节点，这个才是真节点
            else:
                return None

判断一个数是不是2的次方
--------------------

如果一个数是2的多少次方，那么这个数的二进制肯定是 ``10000...`` 这种形式，此时这个数如果减1，那么会变成 ``11111...`` 这种形式。

.. code-block:: python

    if n & (n - 1) == 0:
        return True
    else:
        return False

从array中找到某个元素前面、离这个元素最近的、小于或等于这个元素的元素的下标
---------------------------------------------------------------

文字描述起来很啰嗦，用数学表达就是有一个array记为 :math:`\{a_i\}` ，对于每一个 `i` 找到

.. math::

    \max\{j | a_j \leq a_i, 0 \leq j < i\}

暴力做法就是数学表达式本身

1.  取出第i个元素前面的所有元素
2.  筛选出比第i个元素小或者等于的所有元素
3.  取出下标最大的那个元素的下标

数学表达式本身代表的做法是无论array的情况是怎样，复杂度都是 :math:`O(n^2)` 。可以稍加改进，变成

1.  看第i-1个元素是否小于或等于第i个元素

    -   是，那么恭喜找到了
    -   不是，到下一步

2.  看第i-2个元素是否小于或等于第i个元素

    -   是，那么恭喜找到了
    -   不是，到下一步

3.  ...
4.  看第0个元素是否小于或等于第i个元素

    -   是，那么恭喜找到了
    -   不是，那么也没了，说明根本不存在这样的元素

复杂度最差情况是 :math:`O(n^2)` ，出现在array正好单调递减的情况；最好情况 :math:`O(n)` ，出现在array正好单调递增的情况。

再进一步考虑这个比较过程有没有可以缓存的地方 [#]_ 。

.. [#] 这里我再想想怎样从暴力想到stack……

用单调递增stack可以实现 :math:`O(n)` 。

.. code-block:: python

    # 摘自907

    stack = [] # 单调递增stack，里面存的是 (i, v) 其中v是从底到顶单调递增的
    nearestLessOrEqualElementPosition = [-1] * len(A) # 初始化数组，nearestLessOrEqualElementPosition[i] 表示的是，第i个元素前面最近的、比第i个元素小或者相等的元素的下标。

    for i, v in enumerate(A):

        while stack != [] and stack[-1][1] > v: # stack顶上的元素比当前元素大
            stack.pop() # 所以要pop掉
        # 出while循环之后，stack要么是空的，要么顶部的那个元素小于等于v，也就定位到了第i个元素前面最近的、比第i个元素小或相等的元素和下标

        if stack == []: # 如果stack空了，说明第i个元素前面不存在比自己小或者相等的元素，即第i个元素前面的元素全都比自己大
            nearestLessOrEqualElementPosition[i] = -1 # 用-1表示没有
        else: # stack没空，说明前面确实存在小于等于第i个元素的元素，并且最近的元素就刚好在stack顶部
            nearestLessOrEqualElementPosition[i] = stack[-1][0] # 所以找到了，记录一下
        stack.append((i, v)) # 再把当前元素放进stack

话说我居然之前都不记得自己没看答案就自己做出递增递减stack的题目。739是没看答案自己想出来的，结果看到907的时候居然又不会做了。但是一想也可以理解吧，因为739、1019是找元素后面比自己大的元素，而907是倒过来、找元素前面比自己小的元素，但是两个stack的建立方向（也就是遍历array的方向）却是一样的、都是从前往后的。

两种做法应该是可以互相转化的。

.. code-block:: python

    # 摘自739

        class Solution:
            def dailyTemperatures(self, T: List[int]) -> List[int]:
                # stack = [
                #     (0, T[0])
                # ]
                stack = [] # stack里的元素保证从底到顶递减（不是严格递减，可以相等）
                res = [0] * len(T) # 先初始化，每天都假设永远等不到气温比今天高的那天，这样最后不用补0什么的，方便一点

                for i, v in enumerate(T):
                    if stack:

                        while True:
                            if stack:
                                day = stack.pop() # 这里pop了，后面如果发现大于等于今天的气温，记得要放回去
                                if v > day[1]: # 和stack顶部的元素比较，如果今天气温大于这一天的气温，说明那一天找到了离自己最近的、比自己气温高的那一天
                                    res[day[0]] = i - day[0] # 把那一天的值设为今天和那一天的日期之差
                                else: # 发现今天气温小于等于那一天的气温，那么说明那一天至今都没有找到比自己气温高的日子，同时因为stack保证气温递减，所以顶部以下的日子都不用看了，能保证顶部以下的所有日子的气温都大于等于顶部那天的气温。
                                    stack.append(day) # 记得把那一天放回去
                                    stack.append((i, v)) # 再把今天放进去
                                    break # 继续明天
                            else: # stack已经空了，没日子好比较了
                                stack.append((i, v)) # 直接把今天放进去
                                break # 继续明天

                    else: # stack空的话，就直接放进去
                        stack.append((i, v))
                return res # 初始化的好处就是最后直接返回，不用补零什么的

衍生

-   739 找到array中每个元素之后最近的比自己大的元素 递减stack
-   1019 找到链表中每个节点之后最近的比自己大的元素 递减stack

从array中找到某个元素前面、离这个元素最远的、小于或等于这个元素的元素的下标
---------------------------------------------------------------

.. code-block:: python

    # 摘自962

    class Solution:
        def maxWidthRamp(self, A: List[int]) -> int:
            stack = []
            res = 0

            for i, v in enumerate(A):
                if stack == [] or stack[-1][1] > v:
                    stack.append((i, v))

            for j, w in reversed(list(enumerate(A))):

                while stack != [] and stack[-1][1] <= w:
                    res = max(res, j - stack.pop()[0])

            return res

衍生

-   1124 找到满足某个条件的最长substring的长度
-   962 找到 `\max\{j - i | a_i \leq a_j, 0 \leq i < j \leq n - 1\}`

二分搜索
-------

.. code-block:: python

    # 改编自 https://en.wikipedia.org/wiki/Binary_search_algorithm 的伪代码

    def binarySearch(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            else: # 可以加一行这个提前退出
                return middle

        return -1

.. note:: 如果array不是严格递增的，是含有重复的，那么就涉及到返回最左边还是最右边元素下标的问题。

    .. code-block:: python

        # 寻找最左边最先出现的target的下标

        def binarySearchLeftmost(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums)

            while left < right:
                middle = (left + right) // 2
                if nums[middle] < target: # 注意这里是 <
                    left = middle + 1
                else:
                    right = middle

            # 如果存在的话，left就是最左边等于target的元素的下标，但是如果不存在的话你也不知道，所以要判断一下。
            if 0 <= left <= len(nums) - 1: # 防止越界
                if nums[left] == target:
                    return left
                else:
                    return -1
            else:
                return -1

    .. code-block:: python

        # 寻找最右边最晚出现的target的下标

        def binarySearchRightmost(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums)

            while left < right:
                middle = (left + right) // 2
                if nums[middle] > target: # 注意这里是 >
                    right = middle
                else:
                    left = middle + 1

            # 如果存在的话，right - 1就是最右边等于target的元素的下标，但是如果不存在的话你也不知道，所以判断一下为好。
            if 0 <= right - 1 <= len(nums) - 1:
                if nums[right - 1] == target:
                    return right - 1
                else:
                    return -1
            else:
                return -1

衍生

-   704 二分搜索
-   278 找到第一个bad version

区间求和
-------

如果经常需要求 ``nums[i: j]`` 的和，可以先用 ``itertools.accumulate()`` 一次性把所有和都求出来，这样

.. code-block:: python

    integral = [0] + list(itertools.accumulate(nums)) # 前面添一个0，这样方便很多
    assert integral[j] - integral[i] == sum(nums[i: j])

这样 ``nums[i: j]`` 的和就是 ``integral[j] - integral[i]`` 。

再结合 ``set`` 或者 ``Counter`` 就能实现快速查找是否存在substring的和满足某个条件

.. code-block:: python

    # 摘自560

    class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
            integral = [0] + list(itertools.accumulate(nums)) # 做积分
            counter = collections.Counter(integral) # 数每个积分项出现的次数
            res = 0

            for v in integral: # 遍历积分项
                counter[v] -= 1 # 排除当前积分项
                res += counter[v + k] # 查后面后多少项正好是当前项加上k

            return res

衍生

-   974 有多少个substring的和是K的倍数
-   560 有多少个substring的和是K
-   327 有多少个substring的和在某个interval内
-   523 是否存在一个长度至少为2的substring的和是K的倍数
-   1013 有可能把一个array分成三段各自累加和相同的substring吗
-   525 含有等量0和1的substring的最大长度
-   918 循环列表里的最大substring和
-   1171 不停的去掉链表里累加和是0的substring
-   926 数前后两半substring中 ``0`` 和 ``1`` 的个数
-   1208 累加和小于等于K的最长substring的长度

.. note:: 这种方法又叫前缀和 aka. prefix sum。

二维区间求和
----------

也叫二维前缀和，是一维前缀和的推广。和一维前缀和的关系就像是一元概率分布和联合概率分布的关系。

.. code-block:: python

    # 摘自1314

    class Solution:
        def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
            rowCount = len(mat)
            columnCount = len(mat[0])
            integral = [[0] * (columnCount + 1) for _ in range(rowCount + 1)]

            for rowIndex in range(1, rowCount + 1):

                for columnIndex in range(1, columnCount + 1):
                    integral[rowIndex][columnIndex] = mat[rowIndex - 1][columnIndex - 1] + integral[rowIndex - 1][columnIndex] + integral[rowIndex][columnIndex - 1] - integral[rowIndex - 1][columnIndex - 1]

            ...

无向图中判断两个节点之间是否有路径联通
--------------------------------

就是union find。首先需要一个dict或者array来存节点之间的连接关系，在 ``(key, value)`` 中， ``key`` 表示节点， ``value`` 表示这个节点的父节点。如果两个节点在同一个树中，说明它们之间有路径联通。判断两个节点是否在同一个树中的问题可以等效为判断两个节点所在的树的根节点是否是同一个节点的问题。

.. code-block:: python

    # 改编自1020

    class Solution:
        def union(self, mapping: dict, p: Type, q: Type) -> None: # 建立连接关系
            rootOfP = self.root(mapping, p) # 找到p所在树的根节点
            rootOfQ = self.root(mapping, q) # 找到q所在树的根节点
            mapping[rootOfP] = rootOfQ # 把p所在的树的根节点贴到q所在的树的根节点上

        def isConnected(self, mapping: dict, p: Type, q: Type) -> bool: # 判断两个节点之间是否存在路径相连
            return self.root(mapping, p) == self.root(mapping, q) # 只要判断两个节点是否在同一个树里就可以了，等效为判断两个节点所在树的根节点是否是同一个节点

        def root(self, mapping: dict, r: Type) -> Type: # 得到某个节点所在树的根节点

            while r != mapping[r]: # 如果当前节点的父节点不是自身，说明当前节点不是根节点
                mapping[r] = mapping[mapping[r]] # 这一句话是避免树过深的关键
                r = mapping[r]

            return r

还有一些用法，比如得到每个组里的所有节点

.. code-block:: python

    # 改编自1202

    rootClusterMapping = {}

    for k, v in mapping.items():
        v = self.root(mapping, v)
        if v not in rootClusterMapping:
            rootClusterMapping[v] = {k}
        else:
            rootClusterMapping[v].add(k)

这样就得到了一个 ``dict`` ，其中key是每个组的root，value是一个 ``set`` ，表示这个组包含的所有节点。

再用 ``rootClusterMapping.values()`` 就得到了每个连通区域里的所有节点了。

衍生

-   200 孤立岛屿的个数
-   1034 描出边界

最长公共subsequence
------------------

.. code-block:: python

    # 摘自1035

    class Solution:
        def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
            A = [0] + A
            B = [0] + B
            dp = [[0] * len(B) for _ in range(len(A))]

            for i, v in enumerate(A[1: ], 1):

                for j, w in enumerate(B[1: ], 1):
                    if v == w:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            return dp[-1][-1]

衍生

-   1035 从奇怪的题设背景里提取出最长公共subsequence的核心问题
-   1143 最长公共subsequence

差量更新
-------

假设窗口的长度是k，移动到第i个格子的时候，要

-   减去第i-1个格子的delta
-   加上第i-1+k个格子的delta

比较恶心的是必须要处理初始条件。当然也可以不处理初始条件，不过之后你就要处理烂尾条件。

衍生

-   239 摘取长度为k的窗口里的最大数字

进制转换
-------

思路就是不停地整除，每次取商再整除，最后把每次整除得到的余数倒过来排列。

.. code-block:: python

    # 摘自504

    class Solution:
        def convertToBase7(self, num: int) -> str:
            if num == 0:
                return "0"
            elif num < 0: # 负数的话
                return "-" + self.convertToBase7(abs(num)) # 就转换它的绝对值，再在前面加一个负号
            else: # 正数
                res = [] # 用来记录余数
                
                while num != 0: # 不停地整除7，直到被除数是0为止
                    res.append(num % 7) # 记下余数
                    num = num // 7 # 商变成新的被除数

                return "".join(map(str, reversed(res))) # 结果就是每次整除的余数倒序排列

找到直方图里的第n个数
------------------

.. code-block:: python

    # 改编自1093

    countDown = n

    for i, v in enumerate(count):
        if v != 0:
            if countDown - v <= 0: # 说明第n个数在这一堆里
                return i
            else: # 说明第n个数在后面的堆里
                countDown = countDown - v

得到一个自然数的所有因数
---------------------

暴力做法是从1遍历到n、然后一个一个判断 ``n % i`` 是否等于0，复杂度 `O(n)` 。

但是因为因数都是成对出现的 [#]_ ，也就是说如果找到了一个因数 `k` ，那么 `n / k` 也必然是n的一个因数（注意判断是否重复），所以没有必要遍历到n。从1遍历到 `\lceil\sqrt{n}\rceil` 就够了。复杂度 `O(\ln n)` 。

.. code-block:: python

    def divisors(n: int) -> set:
        factors = {} # 用set可以过滤掉重复的因数

        for i in range(1, math.ceil(n) + 1):
            if n % i == 0: # 发现i是因数
                factors.add(i)
                factors.add(n // i) # n // i也是n的某个因数

        return factors

.. [#] https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/

衍生

-   829 找n的所有奇因数

把array中连续的重复元素分组
------------------------

把形如 ``aaaaabbcccc`` 的array变成 ``["aaaaa", "bb", "cccc"]`` 。

.. code-block:: python

    # 改编自443

    class Solution:
        def compress(self, characters: str) -> List[str]:
            res = []
            lastCharacter = characters[0] # 前一个连续的重复字符串里的字符
            lastCharacterPosition = 0 # 前一个连续的重复字符串在原字符串里开始的位置

            for i, v in enumerate(characters[1: ] + "\x00", 1): # 最后追加一个dummy char，省得出迭代之后再处理
                if v != lastCharacter: # 发现当前字符和前面不一样了，说明上一个连续的重复字符串到这里结束了
                    res.append(lastCharacter * (i - lastCharacterPosition))
                    lastCharacter = v
                    lastCharacterPosition = i

            return len(res)

这件事情也可以用 ``itertools.groupby()`` 来做。 ``groupby()`` 返回一个迭代器，每次 ``next()`` 返回一个tuple ``(v, it)`` ，其中 ``v`` 是重复的那个元素， ``it`` 是另一个迭代器， ``v`` 连续出现几次， ``it`` 就会返回几次 ``v`` 。有点像 ``itertools.repeat(v, v出现的次数)`` 。

.. code-block:: python

    list(map(lambda v: "".join(v[1]), itertools.groupby("aaaabbccc")))

衍生

-   38 数数列前一项每个元素连续出现的次数和元素连接在一起形成当前项
-   443 数字符串里连续的重复元素来压缩字符串

Diff
------

.. code-block:: python

    # 摘自236

    for i in range(min(len(routeToP), len(routeToQ))):
        if routeToP[i].val != routeToQ[i].val:
            return routeToP[i - 1]
    else: # for循环顺利走完没有中途break。说明出现了包含关系
        return routeToP[i]

Tokenize
--------

.. code-block:: python

    # 摘自224

    import re

    patternString = "".join([
        r"(0|[1-9][0-9]*)", # group1 数字
        r"|(\+|-)", # group2 加号和减号
        r"|(\(|\))"
        ]) # group3 括号
    pattern = re.compile(patternString) # 编译pattern，这样会快
    tokens = collections.deque(v.group() for v in pattern.finditer(s)) # 因为这个题里类别比较少，所以这里就不归类了，直接在evaluate的时候归类

甚至还可以给类别起名字，同时得到匹配了哪个类别

.. code-block:: python

    patternString = r"(?P<Number>0|[1-9][0-9]*)" + # group1 数字
        r"|(?P<Operator>\+|-)" + # group2 加号和减号
        r"|(?P<LeftParenthese>\()" # group3 左括号
        r"|(?P<RightParenthese>\))" # group4 右括号
    pattern = re.compile(patternString)
    tokens = [
        (
            v.group(), # 匹配了什么字符串
            v.lastgroup, # 匹配了哪个类别。如果匹配到了加号，就是 'Operator'
        ) for v in pattern.finditer(s)
    ]

图的广度优先搜索
---------------

和二叉树的广度优先搜索差不多的，因为二叉树本质上也算一个图。不同之处在于，二叉树是树，是不含循环的，所以不需要处理重复遍历的问题，但是图需要当心重复遍历的问题。

解决办法非常简单，就是额外维护一个集合，用来记录已经遍历到的节点

.. code-block:: python

    # 改编自863

    class Solution:
        def distanceK(self, root: TreeNode, target: TreeNode, K: int):
            graph = {} # 这里假设图已经按照关联列表的方式存好了，key是节点，value是和这个节点直接相连的节点集合
            queue = collections.deque([root]) # 将要遍历的节点
            traveled = set() # 已经遍历过的节点
            distance = 0

            while queue:
                # 运行到这里的时候，queue里就是距离起点正好是distance的所有节点
                length = len(queue)

                for _ in range(0, length):
                    v = queue.popleft() # 遍历到当前节点了
                    queue.extend(filter(lambda v: v not in traveled, graph.get(v, set()))) # 可能v不和任何节点直接相连，所以要处理不存在key的情况
                    # 这里可以对当前节点做其他事情
                    traveled.add(v) # 做完之后，表明当前节点已经被遍历过了，加入已遍历节点集合，防止下次重复遍历

                distance += 1

            return list(queue)

和二叉树的广度优先、按层遍历的代码高度相似。

衍生

-   1162 离陆地距离最远的海水
-   934 两个岛之间造最短的桥
-   133 复制图

图的深度优先搜索
---------------



``Node`` 形式表示的图转换成关联集合表示的图
--------------------------------------

所谓 ``Node`` 形式就是整个图用一个初始节点表示

.. code-block:: python

    class Node:
        def __init__(self, val: int, neighbors: List[Node]):
            self.val = val
            self.neighbors = neighbors

如要转换成类似

::

    {
        1: {2, 4},
        2: {1, 3},
        3: {2, 4},
        4: {1, 3}
    }

这样的 `关联列表 <https://www.python.org/doc/essays/graphs/>`_ 表示的图，可以用广度优先来做

.. code-block:: python

    # 改编自133

    class Solution:
        def nodeToGraph(self, node: Node) -> dict:
            if node:
                graph = {}
                queue = collections.deque([node])
                traveled = set()

                while queue:
                    length = len(queue)

                    for _ in range(0, length):
                        node = queue.popleft()
                        graph[node.val] = set(map(lambda n: n.val, node.neighbors))

                        for neighbor in node.neighbors:
                            if neighbor.val not in traveled:
                                queue.append(neighbor)
                        # 也可以写成
                        # queue.extend(filter(lambda n: n.val not in traveled, node.neighbors))

                        traveled.add(node.val)

                return graph
            else:
                return {}

.. note:: 我觉得关联 **列表** 这个说法很有问题，用列表来存和某个节点相连的节点的做法也很有问题，比如

    ::

        {
            1: [2, 4],
            2: [1, 3],
            3: [2, 4],
            4: [1, 3]
        }

    因为和某个节点相连的其他节点其实并没有什么先后顺序。所以我觉得更好的方法是关联 **集合** 而不是关联列表。

    如果非要用列表的话（比如133强制要求你复制后的图里 ``neighbors`` 顺序和原节点一模一样），也超级简单啊，把

    .. code-block:: python

        graph[node.val] = set(map(lambda n: n.val, node.neighbors))

    改成

    .. code-block:: python

        graph[node.val] = list(map(lambda n: n.val, node.neighbors))

    就好了。

衍生

-   133 复制图

区间 `[1, n]` 中完全平方数的个数
-----------------------------

是 `\lfloor\sqrt{n}\rfloor` 个。

.. code-block:: python

    math.floor(math.sqrt(n))

衍生

-   319 最后有多少盏灯是开着的

.. note:: 简单证明 `[1, n] \cup N` 中有 `\lfloor\sqrt{n}\rfloor` 个完全平方数

    假设 `m^2` 是小于等于 `n` 的最大的完全平方数，那么区间 `[1, n] \cup N = {1, 2, 3, ..., n}` 当中，一定包含了

    .. math::

        1^2, 2^2, ... , (m - 1)^2, m^2

    这些完全平方数，总共正好 `m` 个。所以接下来要探究 `m` 和 `n` 的关系。根据刚才的假设

    .. math::

        m^2 \leq n < (m + 1)^2

    所以

    .. math::

        m \leq \sqrt{n} < m + 1

    正好就是 `\lfloor\sqrt{n}\rfloor` 的定义。

筛法
----

`O(n \ln n)` 得到 `[1, n)` 中素数的个数、或者 `[1, n)` 中某个数字是否是素数。

.. code-block:: python

    # 摘自204

    class Solution:
        def countPrimes(self, n: int) -> int:
            if n <= 2:
                return 0
            else:
                isPrime = [True] * n # isPrimes[i]用来标记i是不是素数。一开始假定全部都是素数
                isPrime[0] = False
                isPrime[1] = False # 0和1不考虑

                for i in range(2, math.floor(math.sqrt(n)) + 1): # 从2开始遍历
                # for i in range(2, n): # 其实不需要从2到n，到ceil(sqrt(n))就够了。为什么我也没想通
                    if isPrime[i] == True: # 发现i是素数

                        for j in range(i * i, n, i): # 遍历k * i
                        # for j in range(i * 2, n, i): # 这里也不需要从i * 2开始，直接从i^2开始就可以了。为什么我也没想通
                            isPrime[j] = False # 把k * i标记为非素数

                return sum(isPrime)

衍生

-   204 数 `[1, n)` 中有多少个素数
-   1175 把素数放到素数下标的位置

取出个十百千位
------------

.. code-block:: python

    # 摘自12

    thousand = n // 1000 % 10 # 千位
    hundred = n // 100 % 10 # 百位
    ten = n // 10 % 10 # 十位
    one = n // 1 % 10 # 个位

推广一下，取出第 `k` 位可以用

.. math::

    \left\lfloor{n \over 10^k}\right\rfloor \bmod 10

再推广一下，取出 `b` 进制下的第 `k` 位可以用

.. math::

    \left\lfloor{n \over b^k}\right\rfloor \bmod b

前缀树
------

节点的定义

.. code-block:: python

    class Node:
        def __init__(self):
            self.children: Dict[str, Node] = {}
            self.value: Any = None

后缀列表
-------

一个长度为 `n` 的字符串 ``s`` 的排名列表 ``ranks[i]`` 表示以第 `i` 个字符开始、到最后的后缀在所有后缀里面、按字典序从小到大排序排第 ``ranks[i]`` 。

怎么构造呢？有个叫做 `倍增构造法 <https://www.cnblogs.com/SGCollin/p/9974557.html>`_ 的算法。

