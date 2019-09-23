r"""
.. default-role:: math

给一个字符串 ``s``、一个全是数对的array `\{(i, j)\}` ，这个array里的每个元素 `(i, j)` 表示字符串 ``s`` 里面的两个字符 ``s[i], s[j]`` 可以互换位置，那么经过若干次互换（也可能不互换）之后能得到的字典顺序最小的字符串是什么？

超级有意思的一道题。先想一想，如果array里面有

::

    (i, j)
    (j, k)

说明 ``a[i]`` 和 ``a[j]`` 可以互换位置、 ``a[j], a[k]`` 可以互换位置，那么其实说明这三个字符 ``a[i], a[j], a[k]`` 都可以互换位置。

所以我们首先要搞清楚哪些字符可以随便换位置，这样的字符可以成很多组，比如

::

    (i, j)
    (j, k)
    (m, n)
    (n, q)

说明 ``a[i], a[j], a[k]`` 可以互换位置、 ``a[m], a[n], a[q]`` 可以互换位置，但是 ``a[i], a[j], a[k]`` 中的某个字符 和 ``a[m], a[n], a[q]`` 中的某个字符不能互换位置。

这样因为 ``a[i], a[j], a[k]`` 可以互换位置，所以我们给 ``a[i], a[j], a[k]`` 这三个字符按字典顺序排序，排好之后假设变成了 ``x, y, z`` ，再放回到原字符串 ``s`` 里面，也就是令

::

    a[i] = x
    a[j] = y
    a[k] = z

同理因为 ``a[m], a[n], a[q]`` 可以互换位置，我们也给这三个字符按字典顺序从小到大排序，排好之后，放回到原字符串 ``s`` 里面。

举个例子，假设字符串是 ``dcab`` ， ``pairs = {(0, 3), (1, 2)}`` ，那么

::

    d c a b a
    ^     ^ ^---可以互换位置
      ^ ^    ---可以互换位置

首先我们提取出第一组 ``d, b, a`` ，按字典顺序排好之后变成 ``a, b, d`` ，放回字符串的原位置

::

    a b c a d
        ^ ^  ---可以互换位置

第一组排好了，该排第二组了，提取出第二组里的所有字符 ``c, a`` ，同理按字典顺序排好之后是 ``a, c`` ，放回字符串的原位置

::

    a b a c d

这样就排好了。

是不是有一点union find的味道？
"""

from typing import *

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 先用union find得出哪些组的字符可以互换位置
        mapping = {} # union find需要用到的树状图，这里用dict来表示树状图
        res = list(s) # python里面的字符串是不可变的，不能通过s[i] = a来设置第i个字符为a，所以要先变成list，之后调整好了，再用.join()合并起来

        for pair in pairs: # 遍历每个pair，把(a, b)连接在一起
            a, b = pair
            mapping[a] = mapping.get(a, a)
            mapping[b] = mapping.get(b, b)
            self.union(mapping, a, b)

        # union find结束之后，我们需要知道有哪些组、每个组里面有哪些位置

        rootClusterMapping = {} # key是这个组的root节点，value是一个set，表示这个组里面有哪些节点。这样rootClusterMapping.values()就能列出所有的组

        for k, v in mapping.items():
            v = self.root(mapping, v)
            if v not in rootClusterMapping:
                rootClusterMapping[v] = {k}
            else:
                rootClusterMapping[v].add(k)

        for cluster in rootClusterMapping.values(): # cluster就是包含了当前这个组里所有节点的set
            charsInThisCluster = list(map(lambda v: s[v], cluster)) # 把这个组里所有可以替换位置的字符提取出来
            sortedCharsInThisCluster = sorted(charsInThisCluster) # 按字典顺序排序

            for index, char in zip(sorted(cluster), sortedCharsInThisCluster): # 按字典顺序排序完成之后再放回原位置
                res[index] = char # s[i] = x

        return "".join(res)

    # union find的俗套代码
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

# s = Solution()
# print(s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]])) # bacd
# print(s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]])) # abcd
# print(s.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]])) # abc