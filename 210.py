"""
.. default-role:: math

给 `n` 门课，课程之间有依赖关系，按怎样的顺序学习才能满足依赖关系

这就和大学里选课是一样的（然而我们学校课程表是钦定的，没有选课）。比如图形学依赖线性代数，意思是上图形学之前，必须保证线性代数学过。

可以把课程表示成节点，比如图形学是一个节点，线性代数是另一个节点。课程之间的依赖关系就表示成节点之间的有向边，比如图形学依赖线性代数，就表示为一条从线性代数指向图形学的有向边。

这时候就应该用拓扑排序了。这里有一篇很好的文章 <https://www.cnblogs.com/bigsai/p/11489260.html> 。做法和BFS、DFS非递归做法一样，都是用一个queue来储存将要遍历的节点，不断从queue的前面取得节点，并且在遍历节点的过程中把更多的待遍历节点放到queue的后面。

queue里面的节点都是现在可选的课程，也就是没有依赖、或者依赖课程都已经上过的课程。假设线性代数不依赖任何课程、图形学只依赖线性代数这一门课，那么可以直接上线性代数，上完线性代数之后就可以上图形学了。

当遍历到线性代数的时候，找到依赖线性代数的所有课程，可能有图形学、矩阵论等等课程，把这些课程的入边集合更新一下，删掉线性代数，因为线性代数已经上过了。如果发现入边集合变成空集了，比如图形学，就把这门课放到queue的最后。

最后出来的时候判断一下是不是每门课都上过了。
"""

from typing import *


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outs = dict() # b in outs[a]表示有一条有向边从a指向b，表示课程b依赖课程a
        ins = dict() # a in ins[b]表示有一条有向边从a指向b，表示课程b依赖课程a
        # 出边和入边都要储存，这样方便

        for i in range(numCourses):
            outs[i] = set()
            ins[i] = set()

        for b, a in prerequisites:
            outs[a].add(b)
            ins[b].add(a)

        queue = list(filter(lambda v: len(ins[v]) == 0, ins.keys())) # 先筛选出不依赖任何其他课程的课
        res = [] # 上课顺序

        while queue:
            node = queue.pop(0) # 从queue的前面取出课程，假设叫课程node

            for neighbor in outs[node]: # 遍历依赖课程node的所有课程，比如图形学依赖的线性代数、微积分
                ins[neighbor].remove(node) # 因为课程node已经上过了，所以把依赖项删掉，也就是说把图形学对线性代数的依赖删掉
                if len(ins[neighbor]) == 0: # 删掉依赖项之后，发现新的课也能上了
                    queue.append(neighbor) # 放到待选queue里

            res.append(node)
            outs.pop(node) # 从图里面删掉这门课
            ins.pop(node) # 从图里面删掉这门课

        if len(res) != numCourses: # 出来之后判断一下是不是每门课都已经上过了
            return []
        else:
            return res

s = Solution()
print(s.findOrder(2, [[1, 0]])) # [0, 1]
print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])) # [0, 1, 2, 3]