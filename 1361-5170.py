"""
.. default-role:: math

验证有向图是不是二叉树。

输入的有向图的表示方法有点奇怪，是 `n` 个节点 `[0, n - 1]` ， ``leftChild[i] = j`` 表示有一条有向边从 `i` 指向 `j` ， ``rightChild[i] = j `` 也表示有一条有向边从 `i` 指向 `j` 。

这题坑挺多的。

先把那个奇怪的表示方法转换一下变成我们熟悉的adjacent set的表示形式，也就是出度图，类似 ``outs[0] = {1, 2, 3}`` 这种，表示0这个节点有3条出边，分别指向1、2、3。题目要求是这 `n` 个节点必须全部在同一棵树里，不能是森林，所以还需要判断是否只有一个根节点。根节点的入度是0，所以这时候用入度图方便，比如 ``ins[0] = {1, 2, 3}`` 表示0这个节点有3条入边，分别从1、2、3过来。

这件事搞定之后我们就有了用出度表示的图 ``outs`` 和用入度表示的图 ``ins`` 。找到入度为0的所有节点。必须有且只有一个入度为0的节点，这个节点就是根节点。

从这个根节点出发BFS。回想一下，假设这个图已经是个树了，我们会很放心的把所有的子节点加入到queue里，而无需担心子节点是不是已经被遍历过了（这会导致死循环）。但是在遍历图的时候，为了防止重复遍历导致死循环，在把子节点加入待遍历queue中前，总是会写类似

.. code-block:: python

    if neighbor not in traveled and neighbor not in levelQueue:
        levelQueue.add(neighbor)

的代码。所以我们可以用这个来判断图到底是不是树。如果图是树，那么这个if条件永远都不可能被触发。

最后出去的时候还要判断一下是不是真的遍历了 `[0, n - 1]` 里的每一个节点，因为还可能出现

::

    0 <-> 1, 2 -> 3

这样的包含一个环和一个树的图。虽然满足“只有一个入度为0的节点”，但是它并不是树。
"""

from typing import *

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        outs = {i: set() for i in range(n)} # outs[a] = {b, c, d}表示有三条边从a出去，a -> b, a -> c, a -> d
        ins = {i: set() for i in range(n)} # ins[a] = {b, c, d}表示有三条边进入a，b -> a, c -> a, d -> a

        for i in range(0, n):
            left = leftChild[i]
            right = rightChild[i]

            if left != -1:
                outs[i].add(left)
                ins[left].add(i)
            if right != -1:
                outs[i].add(right)
                ins[right].add(i)

        starts = [i for i in range(n) if len(ins[i]) == 0] # 如果是二叉树，那么根节点的入度是0。找到所有入度是0的节点

        if len(starts) != 1: # 只能有一个根节点
            return False

        queue = [starts[0]] # 从这个单一根节点出发BFS
        traveled = set()

        while queue:
            levelQueue = []

            for node in queue:
                if len(outs[node]) > 2: # 判断是不是“二叉”树，不能是三叉树
                    return False

                for child in outs[node]:
                    if child in traveled or child in levelQueue: # 如果是树，那么每个节点都最多只有一条入边（根节点有0条入边），并且没有环。换句话说，如果对树BFS，那么这条if永远不会被触发，一旦被触发，说明这个有向图不是树
                        return False
                    else:
                        levelQueue.append(child)

                traveled.add(node)

            queue = levelQueue

        if len(traveled) != n: # 最后要判断一下树是否包括了[0, n - 1]里所有节点，因为可能出现0 <-> 1, 2 -> 3这种图
            return False
        else:
            return True

s = Solution()
print(s.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1])) # true
print(s.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1])) # false
print(s.validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1])) # false
print(s.validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1])) # false
print(s.validateBinaryTreeNodes(4, [3,-1,1,-1], [-1,-1,0,-1])) # true