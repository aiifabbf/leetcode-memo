"""
给一组方程、不等式，问是否有解。

很有意思的题目，本质还是union find。两个变量相等可以认为是两个节点之间有连通关系，这样我们可以先处理所有相等方程，然后再处理所有不等方程，一旦遇到矛盾，就输出false。
"""

from typing import *

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        mapping = {}

        for equation in equations: # 第一遍遍历
            if equation[1] == "=": # 先处理等式
                a = equation[0] # 变量1
                b = equation[-1] # 变量2
                mapping[a] = mapping.get(a, a)
                mapping[b] = mapping.get(b, b)
                self.union(mapping, a, b) # 变量1和变量2相等，就是两个节点之间有连通关系

        for equation in equations: # 第二遍遍历
            if equation[1] == "!": # 处理不等式
                a = equation[0]
                b = equation[-1]
                mapping[a] = mapping.get(a, a)
                mapping[b] = mapping.get(b, b)
                if self.isConnected(mapping, a, b): # 说明出现了矛盾，之前认为变量1和变量2是相等的，这里却又发现它们不相等
                    return False # 无解
        else: # 遍历结束，没有出现矛盾
            return True # 有解
        
    def union(self, mapping: dict, p: "Hashable", q: "Hashable") -> None:
        rootOfQ = self.root(mapping, p)
        rootOfP = self.root(mapping, q)
        mapping[rootOfP] = rootOfQ

    def root(self, mapping: dict, p: "Hashable") -> "Hashable":

        while p != mapping[p]:
            mapping[p] = mapping[mapping[p]]
            p = mapping[p]

        return p

    def isConnected(self, mapping: dict, p: "Hashable", q: "Hashable") -> bool:
        return self.root(mapping, p) == self.root(mapping, q)

# s = Solution()
# print(s.equationsPossible([
#     "a==b",
#     "b!=a"
# ])) # false
# print(s.equationsPossible([
#     "b==a",
#     "a==b"
# ])) # true
# print(s.equationsPossible([
#     "a==b",
#     "b==c",
#     "a==c"
# ])) # true
# print(s.equationsPossible([
#     "a==b",
#     "b!=c",
#     "c==a"
# ])) # false
# print(s.equationsPossible([
#     "c==c",
#     "b==d",
#     "x!=z"
# ])) # true