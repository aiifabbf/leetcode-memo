=============
leetcode备忘录
=============

.. default-role:: math

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

其实就是非对称双指针的思路

.. code-block:: rust

    // 摘自392

    fn is_subsequence(s: String, t: String) -> bool {
        let mut seek = 0;
        let s = s.as_bytes();

        for v in t.bytes() {
            if seek == s.len() {
                return true;
            } else {
                if v == s[seek] {
                    seek += 1;
                }
            }
        }

        return seek == s.len();
    }

判断一个array是不是另一个array的substring（连续）
-------------------------------------------

这要用 `KMP`_ 。

这就很奇怪，DP里面往往是subsequence更难做，然而这里却是substring更难。

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

衍生

-   255 验证是否是二分搜索树的先根遍历
-   331 验证是否是先根遍历路径

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

也可以借助stack，然后迭代，虽然写起来代码很少，但是很难理解。

我觉得模拟函数调用栈的方法好理解一点。但是不典型，代码就不放在这里了。如果真的想知道怎么做的话，看 `94题 <./94.py>`_ 的代码吧。

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

    如果只给先根和后根，却不能唯一确定一个二叉树。这是很奇怪的事情。我也不知道为什么。

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

那么后根遍历能不能不用递归呢？可以的。只需要把前根遍历的迭代做法稍加改动就可以了

-   前根遍历迭代做法里面，是先放 ``right`` 、再放 ``left`` ，这里改成先放 ``left`` 、再放 ``right``
-   最后把结果颠倒一下

.. code-block:: python

    摘自145

    class Solution:
        def postorderTraversal(self, root: TreeNode) -> List[int]:
            if root:
                stack = [root]
                res = []

                while stack:
                    node = stack.pop()
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)

                    res.append(node)

                return res[:: -1]
            else:
                return []

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

更简单的方法是，中根遍历这个树，看遍历结果是不是严格递增的。

.. note:: 似乎BST和二叉树中根遍历严格递增是充要条件。但是我没法证明。

    BST推出中根遍历严格递增肯定是对的。

    中根遍历严格递增能不能推出BST我真的不知道。能否举一个中根遍历严格递增但是却不是BST的例子呢？好像举不出例子。

    `维基百科 <https://en.wikipedia.org/wiki/Binary_search_tree#Verification>`_ 上也说了中根遍历可以用来验证BST。

    说明这两个确实是充要条件。惊了。

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

暴力做法是搜索，复杂度 :math:`O(n^2)` 。用单调递减stack可以做到 :math:`O(n)`

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

遍历单向链表
-----------

统计链表的长度

.. code-block:: python

    head = sentinel.next
    index = 0

    while head:
        # 此时head是第index个节点，可以在不确定长度的情况下做点什么事情

        index += 1
        head = head.next

    # index就是链表的长度

得到链表的第 `k` 个节点

.. code-block:: python

    # 摘自876

    head = sentinel.next

    for i in range(k):
        # head此时是第i个节点，可以做点什么事情

        head = head.next

    # head是第k个节点

插入单向链表
-----------

如果要插入到 `k` 位置，需要先找到第 `k - 1` 个节点，追加在后面。

.. code-block:: python

    # 摘自707

    head = sentinel.next

    for i in range(k - 1):
        head = head.next

    # 出来之后head正好第k - 1个节点

    node = ListNode(val) # 要插入的节点
    node.next = head.next # 这个节点的后一个节点是第k个节点
    head.next = node # 第k - 1个节点后面一个节点是要插入的节点

删除单向链表
-----------

.. note:: 颠倒链表

    .. code-block:: python

        # 摘自206

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

-   739 找到array中每个元素之后最近的比自己大的元素
-   1019 找到链表中每个节点之后最近的比自己大的元素
-   1008 从先根遍历路径重建二分搜索树
-   1475 找到后面第一个比自己小或相等的元素

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

在从小到大拍好序的array里找到一个位置插入 ``target`` ，使得插入 ``target`` 之后，整个array仍然是从小到大排好序的。

不管什么情况，求的都是这个 **插入位置** ，不是元素位置。这样可以少很多麻烦。

.. code-block:: python

    # 找到最左的插入位置

    def bisectLeft(array: List[Type], target: Type) -> int:
        left = 0
        right = len(array)

        while left < right:
            middle = (left + right) // 2
            if array[middle] == target:
                right = middle
            elif array[middle] < target:
                left = middle + 1
            elif array[middle] > target:
                right = middle

        return left

    # 找到最右的插入位置

    def bisectRight(array: List[Type], target: Type) -> int:
        left = 0
        right = len(array)

        while left < right:
            middle = (left + right) // 2
            if array[middle] == target:
                left = middle + 1 # 区别
            elif array[middle] < target:
                left = middle + 1
            elif array[middle] > target:
                right = middle

        return right # 这里left、right都行，反正相等

总结一下

-   如果 ``array[middle] < target`` ，一定收紧左边，所以 ``left = middle + 1``
-   如果 ``array[middle] > target`` ，一定收紧右边，所以 ``right = middle``
-   如果 ``array[middle] == target`` ，看情况

    -   如果是要找到最左插入位置，那么收紧右边
    -   如果是要找到最右插入位置，那么收紧左边

二分还有非常多神奇的应用，有些题目看上去和二分毫无关联。比如1011运货那道题、1631找爬山最省力的路径。

抽象出来，是求使得某个函数 `f` 成立的最小的 `k` 。函数 `f` 有两个性质

-   对于任意 `x \geq k` ，有 `f(x) = 1`
-   对于任意 `x < k` ，有 `f(x) = 0`

这类问题有个明显的特征，一旦我们找到了一个满足条件的 `k` ，那么 `k + 1, k + 2, ...` 一定也满足条件。

衍生

-   704 二分搜索
-   278 找到第一个bad version
-   1011 最少要多少天运完货
-   1552 尽可能稀疏放球
-   528 带权采样
-   436 找开始时间大于等于自己结束时间的区间
-   1283 找到最小的 `n` 使得数组每个元素除以 `n` 之后的累加和大于等于 `t`
-   1631 最省力的爬山路径

区间求和
-------

又叫前缀和 aka. prefix sum。

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
-   930 有多少个和是S的非空substring
-   1371 含有偶数个元音字母的最长substring
-   1310 快速计算任意substring的累积xor
-   303 计算任意substring的累加和
-   1177 有多少个substring能重新排列变成回文
-   437 二叉树里有多少条单向路径累加和正好是target

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

衍生

-   304  计算子矩阵的和
-   1314 计算以某个点为中心的子矩阵的和
-   1074 有多少个子矩阵的和是target

广义的区间累积/前缀和
------------------

前缀和还可以进一步发挥想象力，可以不止做前缀“和”，还可以前缀最大值、后缀最大值。比如 ``maximumBefore[i]`` 定义为 ``array[: i]`` 里的最大值， ``minimumAfter[i]`` 定义为 ``array[i: ]`` 里的最大值。

.. code-block:: python

    # 摘自42

    maximumBefore = [0] # maximumBefore[i]是array[: i]里的最大值

    for v in array:
        maximumBefore.append(max(maximumBefore[-1], v))

    maximumAfter = [0] # maximumAfter[i]是array[i: ]里的最大值

    for v in reversed(array):
        maximumAfter.append(max(maximumAfter[-1], v))

    maximumAfter.reverse() # 最后要颠倒一下

甚至还可以前缀xor、累积xor。太疯狂了。

衍生

-   42  接雨水
-   1310 求任意substring的累积xor
-   1738 求子矩阵的最大累积xor

线段树
------

用 ``integrals[j] - integrals[i] == sum(array[i: j])`` 查询很方便，复杂度 `O(1)` ，但是如果要修改怎么办？只能重新算一遍 ``integrals`` ，复杂度 `O(n)` 。

不用 ``integrals`` 的话，算 ``sum(array[i: j])`` 很麻烦，复杂度 `O(n)` ，但是修改方便， `O(1)` 。

所以这是两个极端。

线段树是折中方案，查询、修改都是 `O(n \ln n)` 。

原理也很简单，和二分搜索树差不多。根节点存 `[l, r)` 的和、也就是 ``sum(array[l: r])`` 。设 `m` 是 `l, r` 的中位数，即 `m = \left\lfloor{l + r \over 2}\right\rfloor` 。

衍生

-   307 求array任意区间的累加和，array里的数频繁修改

无向图中判断两个节点之间是否有路径联通
--------------------------------

就是union find。首先需要一个dict或者array来存节点之间的连接关系，在 ``(key, value)`` 中， ``key`` 表示节点， ``value`` 表示这个节点的父节点。如果两个节点在同一个树中，说明它们之间有路径联通。判断两个节点是否在同一个树中的问题可以等效为判断两个节点所在的树的根节点是否是同一个节点的问题。

.. code-block:: python

    # 改编自1020

    class UnionFindGraph(dict):
        def union(self, p: Hashable, q: Hashable): # 建立连接关系
            rootOfP = self.root(p) # 找到p所在树的根节点
            rootOfQ = self.root(q) # 找到q所在树的根节点
            self[rootOfP] = rootOfQ # 把p所在的树的根节点贴到q所在的树的根节点上

        def isConnected(self, p: Hashable, q: Hashable) -> bool: # 判断两个节点之间是否存在路径相连
            return self.root(p) == self.root(q) # 只要判断两个节点是否在同一个树里就可以了，等效为判断两个节点所在树的根节点是否是同一个节点

        def root(self, r: Hashable) -> Hashable: # 得到某个节点所在树的根节点

            while r != self[r]: # 如果当前节点的父节点不是自身，说明当前节点不是根节点
                self[r] = self[self[r]] # 这一句话是避免树过深的关键
                r = self[r]

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

.. note:: 写了个Rust版的……好难写，我也不知道有没有更好的写法。给hash map加方法真爽啊。

    .. code-block:: rust

        // 摘自1202

        trait UnionFind<'a, T> {
            fn root(&'a self, p: &'a T) -> &'a T; // 强行把这个从T变成&T，但其实对于Copy来说，T和&T性能上没什么差别……
            fn isConnected(&'a self, p: &'a T, q: &'a T) -> bool; // 就当练习一下lifetime吧……
            fn union(&mut self, p: T, q: T);
        } // 这边我不知道怎么把参数从T变成&T

        impl<'a, T> UnionFind<'a, T> for HashMap<T, T>
        where
            T: Hash + Eq + Copy, // 这里也是，不知道怎么去掉Copy
        {
            fn root(&'a self, p: &'a T) -> &'a T {
                // 这里是python里不同的写法。python里面可以在root()里面一边找root、一边优化图结构，但是这里不行，只能只读。
                let mut p = p;

                while self.get(p).unwrap() != p {
                    p = self.get(p).unwrap();
                }

                return p;
            }

            fn isConnected(&'a self, p: &'a T, q: &'a T) -> bool {
                let rootOfP = self.root(p);
                let rootOfQ = self.root(q);

                return rootOfP == rootOfQ;
            }

            fn union(&mut self, p: T, q: T) {
                // 所以把优化图结构的事情移到了这里，不知道这个对性能有什么影响
                let mut p = p;

                while *self.get(&p).unwrap() != p {
                    self.insert(p, *self.get(self.get(&p).unwrap()).unwrap()); // 这一行写的真的很难看，不知道有没有更好的写法
                    p = *self.get(&p).unwrap();
                }

                let rootOfP = p;
                let mut q = q;

                while *self.get(&q).unwrap() != q {
                    self.insert(q, *self.get(self.get(&q).unwrap()).unwrap());
                    q = *self.get(&q).unwrap();
                }

                let rootOfQ = q;

                *self.get_mut(&rootOfP).unwrap() = rootOfQ;
            }
        }

衍生

-   200 孤立岛屿的个数
-   130 矩阵里所有不和边界连通的 ``O`` 变成 ``X``
-   547 有多少个朋友圈
-   684 冗余连接
-   934 造一座连接两个岛的最短的桥
-   990 方程组、不等式组是否有解
-   1020 有多少个格子能走到地图边界
-   1036 巨大的地图里能否从起点走到终点
-   1202 互换字符能得到的最小字典序的字符串
-   1034 描出边界
-   695 最大的岛屿面积

在一维情况下可以退化到区间边界查询，用两个hash map搞定

-   128 从array里挑数字能凑多长的连续整数序列
-   1562 存在 `k` 个连续1的最后一步
-   352 相邻整数组成区间

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
        factors = set() # 用set可以过滤掉重复的因数

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
-   127 转换几次才能转换到那个词
-   1091 从起点到终点的最近距离

图的深度优先搜索
---------------

把queue换成stack就好了。

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

.. note:: 判断一个数字是否是完全平方数可以归约到二分问题。

    先用二分找到满足 `m^2 \geq n` 的最小的 `m` ，然后判断 `m^2` 是否等于 `n` 。

    .. code-block:: rust

        // 摘自367

        fn is_perfect_square(n: i32) -> bool {
            let n = n as i64;
            let f = |m: i64| -> bool { m.pow(2) >= n };

            let target = true;
            let mut left = 0;
            let mut right = n;

            while left < right {
                let middle = (left + right) / 2;
                let test = f(middle);
                if target > test {
                    left = middle + 1;
                } else if target < test {
                    right = middle;
                } else {
                    right = middle;
                }
            }

            return left.pow(2) == n;
        }

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

也叫字典树。

节点的定义

.. code-block:: rust

    // 摘自208

    struct Trie {
        value: Option<char>, // 用来标记能否是某个单词的末尾
        children: BTreeMap<char, Trie>, // 用BTreeMap可以保证有序
    }

插入单词。打通一条从根节点到最后一个字符的路径

.. code-block:: rust

    impl Trie {
        fn insert(&mut self, word: String) {
            let mut head = self;

            for v in word.chars() {
                if !head.children.contains_key(&v) {
                    head.children.insert(v, Trie::new());
                }
                head = head.children.get_mut(&v).unwrap();
            }

            head.value = Some('\0'); // 最后一个char上标记一下，表示这边可以终止
        }
    }

查找单词。看是否存在一条路径，并且最后一个节点还要是终止节点

.. code-block:: rust

    impl Trie {
        fn search(&self, word: String) -> bool {
            let mut head = self;

            for v in word.chars() {
                if let Some(child) = head.children.get(&v) {
                    head = child;
                } else {
                    // 走不下去了
                    return false;
                }
            }

            return head.value.is_some(); // 一定要正好在这个char上终止才算数
        }
    }

.. note:: 我怀疑把字典树稍加改动就能变成trie map，直接把key对应的value放在最后一个char对应的节点上，就是让 ``value`` 从表示终止变成直接表示value。

    .. code-block:: rust

        impl TrieMap {
            fn new() -> Self {
                Self {
                    value: None,
                    children: BTreeMap::new(),
                }
            }

            fn insert(&mut self, key: String, value: String) {
                let mut head = self;

                for v in key.chars() {
                    if !head.children.contains_key(&v) {
                        head.children.insert(v, TrieMap::new());
                    }
                    head = head.children.get_mut(&v).unwrap();
                }

                head.value = Some(value);
            }

            fn get(&self, key: &String) -> Option<&String> {
                let mut head = self;

                for v in key.chars() {
                    if let Some(child) = head.children.get(&v) {
                        head = child;
                    } else {
                        return None;
                    }
                }

                return head.value.as_ref();
            }
        }

衍生

-   208 实现前缀树
-   211 用前缀树实现单词查找
-   1032 最后见过的几个字母能否构成单词

后缀列表
-------

一个长度为 `n` 的字符串 ``s`` 的排名列表 ``ranks[i]`` 表示以第 `i` 个字符开始、到最后的后缀在所有后缀里面、按字典序从小到大排序排第 ``ranks[i]`` 。

怎么构造呢？有个叫做 `倍增构造法 <https://www.cnblogs.com/SGCollin/p/9974557.html>`_ 的算法。

线性时间、无额外空间、把array里满足条件的元素全部移动到最后面
-----------------------------------------------------

这个问题叫 `荷兰国旗问题 <https://en.wikipedia.org/wiki/Dutch_national_flag_problem>`_ ，不过我把这个问题叫做“荷叶上的水滴合并”问题哈哈。我自己觉得比什么国旗形象多了。

比如你有个array

::

    0, 0, 0, 0, 3

你想把所有的 ``0`` 都移到array的最后面，如果用暴力的话，就是pop第一个 ``0`` 、push到最后、pop下面一个 ``0`` 、push到最后……array的缺点是pop中间某个元素，后面的元素全部都要顺次往前移动一格，这样复杂度就是 `O(n ^ 2)` 了。

很简单，用 ``left, right`` 表示全 ``0`` 水滴的边界，然后慢慢往后边移动就可以了，期间遇到 ``0`` 就吸收、遇到非 ``0`` 就和水滴最左边的元素交换。

.. code-block:: python

    # 摘自283

    class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            if len(nums) >= 1:
                left = 0 # 水滴的左边界。左闭
                right = 0 # 水滴的右边界。右开

                while right < len(nums):
                    if nums[right] == 0: # 遇到0
                        right += 1 # 吸收
                    elif nums[right] != 0: # 遇到非0
                        nums[left], nums[right] = nums[right], nums[left] # 把右边的非0数和水滴的第一个数字交换位置
                        left += 1
                        right += 1 # 更新水滴边界

            else:
                return

既然是个非对称滑动窗口，写成for更不容易出错

.. code-block:: rust

    let mut left = 0;

    for right in 0..array.len() {
        if f(array[left]) {
            // 遇到满足条件的
            continue; // 吸收
        } else {
            // 遇到不满足条件的
            array.swap(left, right);
            left += 1;
        }
    }

    // 到这里，array[..left]里都是不满足条件的元素，array[left..]里都是满足条件的元素

快速排序的partition阶段用了这个算法。

衍生

-   283 把array里所有的0都移动到array的最后面
-   75  给只含有 ``0, 1, 2`` 的array从小到大排序
-   912 快速排序

固定长度的滑动窗口
----------------

.. note:: 我发现有些人把双指针也叫做滑动窗口……也有道理吧， ``left, right`` 限制住的区域确实能看成一个窗口，但是我不太喜欢这样叫。双指针就是双指针嘛，本质上是greedy。滑动窗口的窗口长度是固定的，不变的。

假设array的长度是 `n` ，窗口的长度是 `k` 。那么

-   初始窗口里所有元素下标的范围是 `[0, k)`
-   窗口左边界的范围是 `[0, n - k + 1)`

    为啥是这样呢，因为最靠右的窗口的右边界正好是 `n` ，窗口长度是 `k` ，所以最靠右的窗口的左边界是 `n - k` 。

窗口边界往右移动一格之后，需要更新窗口，这时候新窗口相对于旧窗口的diff是

-   删除 ``array[i - 1]``
-   加入 ``array[i - 1 + k]``

画个图就很清楚

::

    [________)
    i - 1    i - 1 + k
      [________)
      i        i + k

可以看做是一种差量更新吧。还经常和rolling hash配合使用，比如 `1392题 <https://leetcode.com/problems/longest-happy-prefix/>`_ 。

.. code-block:: python

    # 摘自239

    queue = collections.deque() # queue里面存(array[i], i)。每次从最前面取出最大值的时候，都要检查一下这个最大值到底是不是当前窗口里的，所以一定要存i

    for i, v in enumerate(nums[: k]): # 初始窗口里元素下标范围是[0, k)

        while queue:
            if queue[-1][0] < v:
                queue.pop()
            else:
                break

        queue.append((v, i))

    res = [queue[0][0]] # 初始窗口里的最大值

    for i in range(1, len(nums) - k + 1): # 窗口左边界的范围是[1, n - k]
        v = nums[i + k - 1] # 新加的元素

        while queue:
            if queue[-1][0] < v:
                queue.pop()
            else:
                break

        queue.append((v, i + k - 1))

        while queue:
            if queue[0][1] >= i:
                res.append(queue[0][0])
                break
            else:
                queue.popleft()

我知道这里初始窗口和后面的循环有时候会有重复代码，但是我也不知道怎么去掉。还是不要去掉了，这样比较符合直觉。

衍生

-   239 每个窗口里的最大值
-   480 每个窗口里的中位数
-   1392 最长公共前后缀
-   1343 有多少个窗口平均值大于 `t`

可变长度的滑动窗口
---------------

这个技巧有时候又叫双指针，但是我觉得这个只不过是动态规划的加速手段，为了快速算出 ``dp[j]`` ，保留一部分全局的状态信息在 `i` 里，在计算的 ``dp[j + 1]`` 的时候，可以利用刚才的全局信息。

我不认可这种做法叫做双指针的原因还有一个，就是这里面的两个指针 `i` 和 `j` 是不对等的

-   比如 `i` 指针通常都指在左边界上、 `j` 指针指在右边界上， `i` 可能永远要小于等于 `j`
-   自增 `i` 和自增 `j` 的条件不是对称的

一般的模板是

.. code-block:: rust

    for j in 1..s.len() + 1 {
        // 更新一些什么东西，比如counter啥的，使得counter和现在的s[i..j]相匹配

        // 然后算出以s[j - 1]结尾的满足条件的什么什么，并且移动i、更新counter
    }

``while`` 的版本既要动 ``j`` 又要动 ``i`` ，我实在是写不来，所以不要写 ``while`` 了。

荷兰国旗问题属于这一类。

衍生

-   3   不含重复字符的最长substring
-   424 最多 `k` 次修改机会，能得到多长的、所有字符都一样的substring
-   1004 最多 `k` 次修改机会，能得到多长的、全是1的substring
-   992 有多少个substring中出现了 `k` 种元素
-   76 最短的、包含另一个字符串的substring

对称双指针
---------

自增 `i` 和自增 `j` 条件完全对称的正统双指针。

-   912 合并排序
-   986 合并两个人的空闲时间区间、两个人能一起开会的时间段
-   1229 两个人约时间开会

KMP
-----

有两种解释KMP的角度

-   有限定态状态机 aka. DFA

    Princeton的小红书用了这种角度。

-   ``next`` 数组回退

    坊间流传的角度，国内各大算法教材采用的角度。

两种角度非常相似。虽然我更喜欢DFA的角度，但是我觉得 ``next`` 数组回退的角度比较简单。分为两步

1.  构建 ``next`` 数组
2.  根据 ``next`` 数组匹配、回退

各种教程里面的 ``next`` 数组定义得千奇百怪，而且有的是 ``i + 1`` 有的是 ``i - 1`` ，实在是没有统一的美感。

不要烦了，看我这里的定义： ``next[j]`` 有两个含义，没有 ``j - 1`` ，没有 ``j + 1`` ，就是 ``j``

-   表示 ``pattern[0: j]`` 里（注意左闭右开）的最长的公共前后缀（不含本身）的长度

    啥叫最长公共前后缀，就是某个字符串，既是 ``pattern[0: j]`` 的前缀、也是它的后缀。

    那字符串本身不就既是前缀又是后缀吗？这是trivial的情况，不算数。我们要找的是non-trivial的情况。

    比如假设 ``pattern`` 是

    ::

         A B C D A B D
        0 1 2 3 4 5 6 7

    那么 ``pattern[0: 6]`` 是 ``ABCDAB`` ， ``AB`` 既是前缀、也是后缀，而且是最长的、不是本身的、既是前缀又是后缀的字符串。所以 ``next[6] = 2`` 。

    当然 ``ABCDAB`` 本身既是前缀也是后缀，但是这是trivial的，不算数。

-   表示在匹配过程中，如果出现 ``s[i]`` 和 ``pattern[j]`` 不同的时候， ``j`` 应该回退到 ``next[j]``

    就是匹配过程中，如果出现 ``s[i] != pattern[j]`` ，应该令 ``j = next[j]`` ，再次尝试 ``s[i]`` 是否等于 ``pattern[j]`` 。

    当然如果 ``j`` 已经是0了，那么也回退不到哪里去了，只能让 ``i`` 自增1了。

马上观察到

-   ``next[0]`` 没有定义
-   ``next[1] = 0``

为啥呢？

-   空字符串 ``pattern[0: 0]`` 的最长公共前后缀是本身，但是刚才说了要排除本身，但是空字符串排除了本身还剩什么呢……反正 ``j`` 回退到0的话我们是特殊处理的，所以随便取个数吧，这格就浪费也无所谓。
-   ``pattern[0: 1]`` 长度是1，最长的、不是本身的公共前后缀只能是空字符串

构建 ``next`` 数组其实是动态规划过程，只是用了一个状态变量 ``i`` 来加速DP表的构建。

.. code-block:: rust

        // 摘自28

        let mut next = vec![0, 0]; // next[j]表示，如果当前s[i] != p[j]的话，j要回退到next[j]，再试一次s[i]是否等于p[j]。如果j回退到0之后，s[i]仍然不等于p[0]，那么说明从第一个字符开始就不匹配，只能i += 1了
        let mut i = 0;

        for j in 2..p.len() + 1 {
            if p[j - 1] == p[i] {
                // 可以接在前一个后缀的后面
                i += 1;
            } else {
                // 没法接在前一个后缀的后面，只能往前找找有没有符合条件的
                // 下面这段我到现在都不理解意思，暂时先背下来了

                while i != 0 {
                    i = next[i];
                    if p[j - 1] == p[i] {
                        i += 1;
                        break;
                    }
                }

            }
            next.push(i);
        }

根据 ``next`` 匹配、回退

.. code-block:: rust

    // 摘自28

    let mut i = 0; // i是s上的指针
    let mut j = 0; // j是p上的指针

    while i != s.len() {
        // 将要比较s[i]和p[j]
        if s[i] == p[j] {
            // 如果相等
            i += 1;
            j += 1; // 两个指针同时往下一格移动
            if j == p.len() {
                // j已经移动到pattern的最后了
                return Some(i - p.len()); // 说明找到了substring
            }
        } else {
            // 不相等，试图把j回退到next[j]
            if j == 0 {
                // 但是如果j本身已经是0了，s[i]还是不等于p[0]
                i += 1; // 那么只能比较下一个字符了
            } else {
                // j不是0
                j = next[j]; // 试着回退一次
            }
        }
    }

    return None; // i已经指到最后了，s全部比较完了，都没能找到相同的substring，说明根本不存在

这段就很简单了。

衍生

-   28  实现 ``indexOf()``
-   1392 最长的既是前缀又是后缀的substring

回溯
-----

.. code-block:: rust

    fn backtrack(path: &mut Vec<i32>, choices: &[i32], res: &mut HashSet<Vec<i32>>) {
        if Self::ok(path) {
            // 合理路径
            res.insert(path.clone()); // 加入到结果集合里
            return;
        } else {
            for choice in choices.iter() {
                if Self::valid(path, choice) {
                    // 这一步这样走是合法的
                    path.push(choice); // 做选择
                    Self::backtrack(path, choices, res);
                    path.pop(); // 撤销刚才的选择
                }
            }
        }
    }

衍生

-   22 给 `n` 对括号，所有合法的排列
-   797 从起点到终点的所有路径
-   437 二叉树里有多少条单向路径累加和正好是target
-   37 解数独
-   967 生成所有相邻两位差值是 `k` 的十进制 `n` 位数
-   1286 生成 `n` 个元素的 `r` 的组合
-   79 单词是否在棋盘里
-   131 把字符串切成回文substring有哪些切法
-   980 每个空位都经过且只经过一次的路径有多少个
-   216 `[1, 9]` 里不重复取 `k` 个数字加起来正好等于 `n` 总共有多少种取法
-   1291 生成类似1234、2345这样的数字
-   47 生成 `n` 个元素的 `r` 种无重复排列
-   996 能够使得相邻两个数字之和是完全平方数的排列方式有多少种

有向图中是否有环
--------------

试图拓扑排序，如果拓扑排序不能成功，说明有环，否则没环。

.. code-block:: python

    # 改编自210

    queue = list(filter(lambda v: len(ins[v]) == 0, ins.keys())) # 挑出所有入度是0的节点
    res = [] # 拓扑排序的顺序

    while queue:
        node = queue.pop(0)

        for neighbor in outs[node]: # 遍历能从这个节点出发到达的所有其他节点
            ins[neighbor].remove(node) # 更新图
            if len(ins[neighbor]) == 0: # 把node从图上摘掉之后，可能neighbor的入度也会变成0
                queue.append(neighbor)

        res.append(node)
        outs.pop(node) # 更新图
        ins.pop(node) # 更新图

衍生

-   207 判断有向图里有没有环
-   1494 最快多久毕业
-   210 选课的顺序

点之间的最短距离
--------------

如果只想知道从某一个点出发到每个点的最短距离，建议用 `Dijkstra算法 <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm>`_ ，单起点复杂度 `O(e + v \ln v) \approx O(v^2 + v \ln v)` 。

如果要想一次性知道每个点对的最短距离，建议用 `Floyd算法 <https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm>`_ ，总复杂度 `O(v^3)` ，缺点是要算就要整张图一起算才对，没办法单独算 `i, j` 之间的最短距离。

.. code-block:: rust

    // 摘自1334

    // 初始条件
    for i in 0..n {
        graph[i][i] = 0; // 自己和自己相连
    }

    for relay in 0..n {
        for a in 0..n {
            for b in 0..n {
                graph[a][b] = min(graph[a][b], graph[a][relay] + graph[relay][b]);
            }
        }
    }

判断任意substring（要连续）是否是回文
---------------------------------

用动态规划最好理解。如果 ``s[i..j]`` 是回文、并且左右两边紧邻的两个字符相等、即 ``s[i - 1] == s[j]`` 的话，那么 ``s[i - 1..j + 1]`` 也一定是回文，如图

::

     a x x x x x a
      i         j

缺一不可，充分必要，否则 ``s[i - 1..j + 1]`` 一定不是回文。

所以用 ``dp[i][j]`` 记录 ``s[i..j]`` 是不是回文。

.. code-block:: rust

    // 摘自131

    let s: Vec<char> = s.chars().collect();
    let mut dp = vec![vec![false; s.len() + 1]; s.len() + 1]; // dp[i][j] == true表示s[i..j]是回文

    // 初始条件
    for i in 0..s.len() + 1 {
        dp[i][i] = true; // 空字符串是回文
    }

    // 初始条件
    for i in 0..s.len() {
        dp[i][i + 1] = true; // 单字符也是回文
    }

    for gap in 2..s.len() + 1 {
        for i in 0..s.len() - gap + 1 {
            let j = i + gap;
            // s[i..j]是不是回文、即dp[i][j]是否为true，完全取决于s[i]是不是等于s[j - 1]、并且s[i + 1..j - 1]是不是回文、即dp[i + 1][j - 1]是不是true
            if s[i] == s[j - 1] && dp[i + 1][j - 1] == true {
                dp[i][j] = true;
            }
        }
    }

复杂度 `O(n^2)` 。

衍生

-   131 把字符串切成回文substring的切法
-   132 把字符串切成回文substring最少切多少次

精简零散的区间、合并成大区间、整理区间碎片
------------------------------------

比如 `[1, 2), [2, 3), [3, 4), [1, 5)` 合并成 `[1, 5)` 。

1.  按开始时间排序
2.  依次进入stack，分情况讨论

    -   如果stack空，直接放进去
    -   如果stack不空，比较一下现在要放入的区间和stack顶端的区间

        -   如果两个区间没有交集，还是直接放进去
            比如将要放入 `[2, 3)` ，而stack顶的区间是 `[1, 2)` ，两者没有交集，那么直接把 `[2, 3)` 放进去就好了。

        -   如果有交集，那么先pop、再取两个区间的并集、再放进stack
            比如将要放入 `[2, 4)` ，而stack顶的区间是 `[1, 3)` ，那么先pop，再取并集，变成 `[1, 4)` 再放入stack。

.. code-block:: rust

    // 摘自56

    intervals.sort(); // 按开始时间从小到大排序
    let mut stack = vec![];

    for v in intervals.into_iter() {
        if stack.is_empty() {
            stack.push(v);
        } else {
            if stack.last().unwrap().1 < v.0 {
                // 和stack顶端的区间没有交集
                stack.push(v); // 直接放进去
            } else {
                // 有交集
                let mut merged = stack.pop().unwrap(); // 先pop
                merged.0 = merged.0.min(v.0);
                merged.1 = merged.1.max(v.1); // 再合并
                stack.push(merged); // 再放入
            }
        }
    }

衍生

-   56 精简区间
-   763 把字符串尽可能切成很多substring同时每种字符只在一个substring里出现
-   57 插入并精简区间
-   1288 删掉被其他区间已经包括的区间

最小生成树
----------

空间中有一些点 `\{v_i\}` ，点之间的距离 `d(v_i, v_j)` 是确定的。现在想要用一棵树把所有点都连起来。树的总长度最小是多少？

这就是最小生成树问题。有时候还会绕一个弯问你，一些城市之间修公路，想要连通每个城市，最少要修多少公里公路。

用 `Kruskal算法 <https://en.wikipedia.org/wiki/Kruskal%27s_algorithm>`_ 很好做。把所有的边、一共 `v^2` 条边，按长度从小到大排序，然后每次取最短的边，看这条边如果连接起来会不会让图中出现环，如果不出现环，就放心地加上这条边；如果会出现环，这条边不能取。

.. code-block:: python3

    # 摘自1584

    graph = UnionFindGraph() # 用来判断会不会出现环
    edges.sort(key=lambda v: v[1]) # 按边长从小到大排序
    res = 0 # 最小生成树的总长度

    for (a, b), distance in edges:
        if a not in graph:
            graph[a] = a
        if b not in graph:
            graph[b] = b

        if not graph.isConnected(a, b): # 如果a和b已经连通了，那么再加入(a, b)这条边一定会产生环
            res += distance
            graph.union(a, b)

    return res

微分积分
--------

导数、原函数、积分具有相同的信息，可以互相转换。

微积分是线性的，导数相加再积分，和直接把原函数相加完全一样。

利用积分、微分的线性性质，不记录counter本身，而是记录counter的 **导数** ，或者叫差分，需要counter本身的时候，给导函数积分得到counter本身。

举个例子，假设有个16元素的counter是

::
    0: 0
    1: 0
    2: 2
    3: 2
    4: 2
    5: 1
    6: 1
    7: 1
    8: 0
    9: 1
    10: 1
    11: 1
    12: 2
    13: 2
    14: 2
    15: 0

如果想知道1出现了几次，非常快， `O(1)` 就能查到。但是如果现在要让 `[3, 13)` 里每个数字出现次数都加1，就很慢，要一个一个去加， `O(n)` 才能完成。

因此普通的counter是一种 **查询高效、修改低效** 的结构。如果查询次数远远大于修改次数，那么很快很方便。但是如果修改次数远远大于查询次数，就很慢。

那么存不存在 **修改高效、查询低效** 的counter呢？很简单，就是counter的导数。

counter本身的图画出来是

::

        2                                2
    |--------|                       |--------|
    |        |    1             1    |        |
    |        |--------|     |--------|        |
    |        |        |  0  |        |        |
    |--------|--------|-----|--------|--------|
    2        5        8     9        12       15

counter的导数是这样的

::

    +2
    |                       +1       +1
    |                       |        |
    |--------|--------|-----|--------|--------|
             |        |                       |
             -1       -1                      |
                                              -2

如果想要让 `[3, 13)` 里每个数字都加1，非常快，在导函数的3那里+1、在13那里-1就搞定了， `O(1)` 搞定。

但是要查询 ``counter[3]`` 就很慢，首先要把导函数积分，恢复成原函数，这需要 `O(n)` 时间，再去原函数里查询。

.. note:: 如果要修改和查询速度平衡，用线段树。

衍生

-   1109 每个航班上订了多少张票
-   1589 怎样排序才能使得指定区间内的累加和最大
-   1674 最少修改多少次能使得array左右平衡