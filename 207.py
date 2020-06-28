"""
.. default-role:: math

有 `n` 门课，课之间有依赖关系，比如课0必须要等课1上完之后才能上。问能不能顺利毕业。

本质上就是探测有向图里有没有环。想到拓扑排序算法里面，需要先过滤出所有入度为0的节点，然后依次pop，pop出来之后，把这个节点从图中删除。既然这个节点已经被删除了，那么指向这个节点的所有边、从这个节点出去的所有边也要一起去掉。刚才已经说过这个节点入度为0了，所以这个节点只有出去的边，只要把这个节点出去的边指向的节点调整一下就好了。

调整的时候，有可能指向的那个节点也出现了入度变为0的情况，那么这时候就要把那个节点加入到queue里。

最后queue空了，看是否遍历到所有的节点了。如果还有节点没有遍历到，说明那些节点一定在某个环里。
"""

from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ins = {} # ins[i] = {j}表示节点j指向i
        outs = {} # outs[i] = {j}表示节点i指向j

        for i in range(numCourses):
            ins[i] = set()
            outs[i] = set()

        for v, w in prerequisites:
            outs[w].add(v)
            ins[v].add(w)

        queue = list(filter(lambda v: len(ins[v]) == 0, ins.keys())) # 过滤出所有入度为0的节点，len(ins[v]) == 0表示没有节点指向节点v，所以入度为0
        traveled = set() # 遍历过的节点

        while queue: # 不停从queue里pop节点
            node = queue.pop(0)

            for v in outs[node]: # 删除节点node，调整这个节点指向的其他节点v
                ins[v].remove(node) # 删掉node指向v这条边
                if len(ins[v]) == 0: # 如果发现删掉那条边之后节点v也入度变成0了
                    queue.append(v) # 加入到queue里

            traveled.add(node) # 遍历节点node完成了

        return len(traveled) == numCourses # 看下是不是所有节点都遍历到了


s = Solution()
print(s.canFinish(2, [[1, 0]]))  # true
print(s.canFinish(2, [[1, 0], [0, 1]]))  # false
print(s.canFinish(3, [[1, 0], [1, 2], [0, 1]]))  # false
print(s.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))  # true
