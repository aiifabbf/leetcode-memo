"""
给节点涂色，要求相邻节点不能用同一种颜色，只有四种颜色可用。

我的做法是遍历每个节点，然后看当前节点有没有被涂过，如果被涂过了，就不要管了；如果没有被涂过，就随便选一个和周围节点都不相同的颜色。
"""

from typing import *

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N # res[i]表示第i个节点的颜色，0表示还没有被涂过
        connections = [set() for _ in range(N)] # connections[i]表示第i个节点相邻的节点

        for path in paths: # 先生成connections
            i = path[0] - 1
            j = path[1] - 1
            connections[i].add(j)
            connections[j].add(i)

        for i, v in enumerate(connections): # 遍历节点，把每个节点都涂上颜色
            if res[i] == 0: # 如果发现当前节点还没有被涂过
                usable = {1, 2, 3, 4} # 可用颜色一开始有4种，但是当然不能和周围的节点相同，所以下面要更新这个可用颜色集合

                for neighbor in v: # 遍历当前节点周围相邻的节点
                    if res[neighbor] != 0: # 如果发现有某个节点已经被涂过颜色了
                        usable.discard(res[neighbor]) # 那么表示当前节点不能再涂这个颜色了

                res[i] = usable.pop() # 随便从可选颜色集合中选择一个颜色涂上

        return res

# s = Solution()
# print(s.gardenNoAdj(3, [[1,2],[2,3],[3,1]]))
# print(s.gardenNoAdj(4, [[1,2],[3,4]]))
# print(s.gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
# print(s.gardenNoAdj(4, [[3,4],[4,2],[3,2],[1,3]]))
# print(s.gardenNoAdj(4, [[1,2],[3,4],[3,2],[4,2],[1,4]]))