r"""
.. default-role:: math

得到二叉树里任意一个节点的第 `k` 个祖先

如果是medium难度，按一般的做法就好了。主要就是这两种做法

-   构造方法里面啥也不干，等到查询的时候，一个一个顺着往前找

    这种做法没有空间复杂度，复杂度全在时间复杂度上。如果树平衡，每次查询的时间复杂度是 `O(\ln n)` ，如果树极不平衡（比如就是个链表），时间复杂度是 `O(n)` 。

    所以适合内存少、查询次数特别少的情况。

-   构造方法里面就把从每个节点一直向上到根节点的路径上每个节点全部按顺序存下来，等到查询的时候一下子就给查出来

    这种做法时间复杂度直接就是 `O(1)` 了，而空间复杂度极高，如果树平衡，可能需要 `O(n \ln n)` 的空间，如果树不平衡（比如链表），可能就需要 `O(n^2)` 的空间了。

    所以适合查询次数极多、内存大的情况。

然而，这道题是hard……所以也能猜到了，这两种做法要么爆超时要么爆内存。需要想一种时间和空间平衡的做法。周赛的时候我就在想了，这题的输入规模是 `10^4` ，所以一定是暗示你要找一种每次查询时间复杂度正好是 `O(\ln n)` 的做法。

那么这个 `\ln n` 这一项从哪里来呢……复杂度具有 `\ln n` 项的算法一定是在某处出现了二叉树、或者等比数列的灵魂。第二种做法的cache实在是太大了，有没有办法缩小一点呢？怎样缩小，才能让查询复杂度正好就是 `O(\ln n)` 呢？

第一种方法，每次查询都是跳1格，总共要跳 `n` 次，所以时间复杂度最差是 `O(n)` ，实在是太慢了；而第二种又是直接一下子跳过去，只要跳1次，时间复杂度是 `O(1)` 。有没有办法做到跳 `\ln n` 次呢？

可以的，第一次跳一半、第二次跳一半的一半、……大致意思就是，假如要查第7个祖先，首先我先去找往上数第4个祖先，再从这个祖先开始，往上找第2个祖先，再从这个祖先开始，往上找第1个祖先。

给每个节点建立一个cache，节点node的第 `2^i` 个祖先节点是 ``cache[node][i]`` 。在查找的时候，假设要查找第 `k` 个祖先，先找到小于等于 `k` 的最大的2的次方数，假设是 `2^i` ，直接一步就能跳到node的第 `2^i` 个祖先，就是 ``cache[node][i]`` ，再从这个祖先节点出发，走完剩下的 `k - 2^i` 步就好了。

建立cache的时候用BFS，这样遍历到每个节点的时候都能保证它的每个祖先的cache都已经建立好了。node的第 `2^i` 个祖先节点，实际上就是node的第 `2^{i - 1}` 个祖先节点的第 `2^{i - 1}` 个祖先节点。所以 ``cache[node][i] = cache[cache[node][i - 1]][i - 1]`` 。

这种优化方法叫二叉树抬升binary tree lifting <https://cp-algorithms.com/graph/lca_binary_lifting.html> 。
"""

from typing import *


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.parents = {} # self.parents[i] = j表示i节点的父节点是j
        self.graph = {} # self.graph[i] = {j, k}表示i节点的子节点是j和k
        self.cache = {} # self.cache[i] = [j, k, l]表示i节点的第2^0个祖先节点是j、第2^1个祖先节点是k、第2^2个祖先节点是l

        for i, v in enumerate(parent):
            if v != -1:
                self.parents[i] = v
                if v in self.graph:
                    self.graph[v].add(i)
                else:
                    self.graph[v] = {i}

            self.cache[i] = []

        # 然后BFS，为每个节点都建立祖先节点cache
        queue = [0]

        while queue:
            node = queue.pop(0)

            if node in self.parents:
                head = self.parents[node]
                self.cache[node].append(head)

                # node的第2^i个祖先节点，刚好就是node的第2^(i - 1)个祖先节点的第2^(i - 1)个祖先节点
                # 所以根据cache的存储特点，cache[node]的第i项cache[node][i]刚好就是cache[cache[node][i - 1]][i - 1]
                i = 1

                while i - 1 < len(self.cache[self.cache[node][i - 1]]):
                    self.cache[node].append(self.cache[self.cache[node][i - 1]][i - 1])
                    i += 1

            if node in self.graph:
                queue.extend(self.graph[node])

    def getKthAncestor(self, node: int, k: int) -> int:
        if k == 0:
            return node
        elif k == 1:
            if node in self.parents:
                return self.parents[node]
            else:
                return -1
        else:
            # 得到小于等于k的最小的2^i，第2^i个祖先就是cache[node][i]，再从这个祖先出发，走完剩下的路
            index = k.bit_length() - 1 # 2 ^ floor(log2(k))
            modulo = k - (1 << index) # 巨坑啊，位移的优先级很低的
            if index < len(self.cache[node]):
                return self.getKthAncestor(self.cache[node][index], modulo)
            else:
                return -1

    # def getKthAncestor(self, node: int, k: int) -> int:
    #     if 0 <= k < len(self.ancestors[node]):
    #         return self.ancestors[node][k]
    #     else:
    #         return -1
    # 第一次，想把从每个节点往上一直到根节点经过的所有节点都记录下来。内存爆了。

    # @functools.lru_cache(None)
    # def getKthAncestorCached(self, node: int, k: int) -> int:
    #     if node == -1:
    #         return -1

    #     if node == 0 and k > 0:
    #         return -1

    #     if k == 0:
    #         return node

    #     return self.getKthAncestorCached(self.parents[node], k - 1)
    # 第二次，先不记录所有的节点，而是按需记录，还是爆内存了。

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)


treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(treeAncestor.getKthAncestor(3, 1)) # 1
print(treeAncestor.getKthAncestor(5, 2)) # 0
print(treeAncestor.getKthAncestor(6, 3)) # -1
