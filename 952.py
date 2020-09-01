"""
.. default-role:: math

给许多节点，节点上的值是正整数，如果两个节点值不互质，它们之间就可以建立连接。问最大的网络里有多少个节点。

暴力做法就是两个两个节点之间用gcd判断是否有大于1的最大公因数，如果有就建立连接。但是这样做的复杂度是 `O(n^2)` ，会超时。看输入规模应该是按时寻找 `O(n)` 或者 `O(n \ln n)` 的做法。

可以反过来想，建一个hash map，key是因数，value是含有这个因数的数字，比如 ``map[6] == {6, 12, 24, 60}`` ，每次遇到一个数字，遍历它的每个因数 `i` ，然后去map里找有没有其他的数字和它共享因数，如果有，就在union find图里把它们连起来。假设每个数字的大小是 `k` ，那么这样做的复杂度是 `O(n \sqrt{k})` 。
"""

from typing import *

import math
import collections


class UnionFindGraph(dict):
    def union(self, p: Hashable, q: Hashable):
        rootOfP = self.root(p)
        rootOfQ = self.root(q)
        self[rootOfP] = rootOfQ

    def root(self, p: Hashable) -> Hashable:

        while p != self[p]:
            self[p] = self[self[p]]
            p = self[p]

        return p

    def isConnected(self, p: Hashable, q: Hashable) -> bool:
        return self.root(p) == self.root(q)


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        mapping = UnionFindGraph() # union find图
        divisorNumberMapping = dict() # divisorNumberMapping[v] = {a, b, c}表示a, b, c的有一个因数是v

        for v in A:
            if v == 1:
                continue

            # 自己是自己的因数
            if v not in divisorNumberMapping:
                divisorNumberMapping[v] = set()
            divisorNumberMapping[v].add(v)

            # 和同样有一个因数是v的其他数连接，比如6和12连接，因为12有一个因数是6
            if v not in mapping:
                mapping[v] = v

            for w in divisorNumberMapping[v]:
                if w != v: # 自己和自己连没有意义，要找一个别的数字
                    mapping.union(v, w)
                    break

            # 遍历v的每个因数，O(\sqrt{k})
            for i in range(2, math.ceil(math.sqrt(v)) + 1):
                if v % i == 0 and (v // i) != 1: # 因数是一对一对找的，如果i是v的因数，那么v // i也一定是v的因数
                    if i not in divisorNumberMapping:
                        divisorNumberMapping[i] = set()
                    divisorNumberMapping[i].add(v)

                    for w in divisorNumberMapping[i]:
                        if v != w:
                            mapping.union(v, w)
                            break

                    if (v // i) not in divisorNumberMapping:
                        divisorNumberMapping[v // i] = set()
                    divisorNumberMapping[v // i].add(v)

                    for w in divisorNumberMapping[v // i]:
                        if v != w:
                            mapping.union(v, w)
                            break

        counter = collections.Counter(
            mapping.root(k) for k in mapping) # 每个组里有多少个节点
        return max(counter.values())


s = Solution()
print(s.largestComponentSize([4, 6, 15, 35])) # 4
print(s.largestComponentSize([20, 50, 9, 63])) # 2
print(s.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39])) # 8
