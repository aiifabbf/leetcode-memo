"""
找到无向图中的重复连接

所谓重复连接就是，如果删除这个连接，不影响这两个节点之间连通关系的连接。

做法还是union find，很简单，遍历所有连接，如果发现连接两端的两个节点已经是连通的了，那么就是这个连接了；如果两个节点不是连通的，就建立连接。
"""

from typing import *

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mapping = {}

        for connection in edges:
            a = connection[0]
            b = connection[1]
            mapping[a] = mapping.get(a, a)
            mapping[b] = mapping.get(b, b)
            if self.isConnected(mapping, a, b): # 连接两端的两个节点已经是连通的了
                return connection # 那这个连接就是重复的了
            else:
                self.union(mapping, a, b) # 不然就建立连接

    def union(self, mapping: dict, p: "Hashable", q: "Hashable") -> None:
        rootOfQ = self.root(mapping, q)
        rootOfP = self.root(mapping, p)
        mapping[rootOfP] = rootOfQ

    def root(self, mapping: dict, p: "Hashable") -> "Hashable":

        while p != mapping[p]:
            mapping[p] = mapping[mapping[p]]
            p = mapping[p]

        return p

    def isConnected(self, mapping: dict, p: "Hashable", q: "Hashable") -> bool:
        return self.root(mapping, p) == self.root(mapping, q)

# s = Solution()
# print(s.findRedundantConnection([[1,2], [1,3], [2,3]])) # [2, 3]
# print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])) # [1, 4]