"""
找到有向图中满足下列性质的节点 :math:`a_i`

-   这个节点没有向外的边
-   其他所有的节点都有边指向这个节点

一开始的想法是用一个NxN矩阵来存边的方向，但是觉得有点麻烦。

改成了用两个HashMap，key是节点编号，value是一个HashSet，里面存从这个节点出去的所有边的目标节点、进入这个节点的所有边的源节点。
"""

from typing import *

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        inBound = {} # 记录指向每个节点的源节点
        outBound = {} # 记录每个节点向外指向的目标节点

        for v in trust:
            outBound[v[0] - 1] = outBound.get(v[0] - 1, set()) | {v[1] - 1}
            inBound[v[1] - 1] = inBound.get(v[1] - 1, set()) | {v[0] - 1}

        tempSet = set(range(N))

        for i in range(N):
            tempSet.remove(i)
            # if (i not in outBound) and (i in inBound) and (inBound[i] == tempSet):
            if (i not in outBound) and (inBound.get(i, set()) == tempSet):
                # print(inBound, outBound)
                return i + 1
            else:
                tempSet.add(i)
        else:
            # print(inBound, outBound)
            return -1

# s = Solution()
# assert s.findJudge(2, [[1, 2]]) == 2
# assert s.findJudge(3, [[1, 3], [2, 3]]) == 3
# assert s.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
# assert s.findJudge(2, [[1, 2], [2, 1]]) == -1
# assert s.findJudge(1, []) == 1