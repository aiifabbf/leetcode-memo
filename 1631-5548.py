"""
.. default-role:: math

在矩阵里寻找从左上角走到右下角最省力的路径。所谓最省力不是传统的路径上节点值的和最小，而是路径上任意两个相邻节点的差值的最大值最小。

比如

::

    1 2 2
    3 8 2
    5 3 5

最省力的路径是

::

    1 2 2
    |
    3 8 2
    |
    5-3-5

花费的力气是2，因为路径上任意两个相邻节点的差值的最大值是2。

我要二分PTSD了……没错，这个题又是二分搜索。用高深的话来说，是个极值表述归约到判定表述的问题。

对于这种一下子想不到方法的题目，可以尝试把问题表述转换一下，转换成判定问题表述。比如这题原来的表述是要寻找最大值，是一个极值问题。可以想一下，如果这个问题这样问“能否花费不超过 `n` 的力气从起点走到终点”，是不是会简单一点？

确实变简单了，BFS一下马上就能知道能不能花费不超过 `n` 的力气到达终点。复杂度是 `O(v)` 。

那么现在我们已经解决了“能否花费不超过 `n` 的力气从起点走到终点”这个问题，抽象一点说，我们有了一个判定函数 ``f: int -> bool`` 告诉我们能不能花费不超过 `n` 的力气从起点走到终点。 `f(3) = 1` 表示可以花费不超过3的力气走到终点。

观察到 `f(n)` 有这样一个性质：一旦我们找到了某个 `k` 使得 `f(k) = 1` ，那么 `f(k + 1)` 也一定等于1、 `f(k + 2)` 也一定等于1……为啥？挺显然的，如果你能花费不超过3的力气走过去，那么花费的力气是3或者2或者1或者0，都是小于4的，所以一定能花费不超过4的力气走过去。

有了这个 `f(n)` 之后，怎样才能帮助我们解决原来的找极值问题呢？我们发现原问题就是要我们找到能使得 `f(n) = 1` 的那个最小的 `n` 。

::

    0, 1, ..., k - 1, k, k + 1, k + 2, ...
                    [--------------------- 行
    ----------------) 不行

把 `f(n)` 写成array的感觉

::

    0, 1, ..., k - 1, k, k + 1, k + 2
    0, 0, ..., 0    , 1, 1    , 1      f(n)

你看，这不就转化到在单调递增array里二分找到最靠左的1出现的位置了吗？

那么复杂度怎么样呢？为了算 `f` 好像复杂度挺高啊，是 `O(v)` 。不用担心，只需要调用 `\ln` 次 `f` ，不会很多的。即使是 `10^9` ， `\log_2 10^9` 也降到了30左右。遇到 `O(\ln n)` 就像常数一样看待就好了。
"""

from typing import *


class Solution:
    # 失败的back track尝试
    # def minimumEffortPath(self, heights: List[List[int]]) -> int:
    #     matrix = heights
    #     rowCount = len(heights)
    #     columnCount = len(heights[0])
    #     if rowCount == 1 and columnCount == 1:
    #         return 0

    #     path = []
    #     effort = [0]
    #     target = max([
    #         abs(heights[0][i] - heights[0][i - 1]) for i in range(1, columnCount)
    #     ] + [
    #         abs(heights[i][0] - heights[i - 1][0]) for i in range(1, rowCount)
    #     ])
    #     # res = [float("inf")]
    #     res = [target]
    #     seen = set()
    #     Solution.backtrack(path, seen, effort, heights, res)
    #     return res[0]

    # @staticmethod
    # def backtrack(path: List[Tuple[int, int]], seen: Set[Tuple[int, int]], effort: List[int], matrix: List[List[int]], res: List[int]):
    #     rowCount = len(matrix)
    #     columnCount = len(matrix[0])

    #     if effort[0] >= res[0]:
    #         return

    #     if len(path) != 0 and path[-1] == (rowCount - 1, columnCount - 1):
    #         if effort[0] < res[0]:
    #             res[0] = effort[0]
    #             print(res[0])
    #             return
    #     else:
    #         if len(path) == 0:
    #             path.append((0, 0))
    #             seen.add((0, 0))
    #             Solution.backtrack(path, seen, effort, matrix, res)
    #             seen.remove((0, 0))
    #             path.pop()
    #         else:
    #             neighbors = [
    #                 (path[-1][0] + 1, path[-1][1]),
    #                 (path[-1][0], path[-1][1] + 1),
    #                 (path[-1][0] - 1, path[-1][1]),
    #                 (path[-1][0], path[-1][1] - 1),
    #             ]

    #             for neighbor in neighbors:
    #                 if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount and neighbor not in seen:
    #                     newEffort = [max(effort[0], abs(matrix[neighbor[0]][neighbor[1]] - matrix[path[-1][0]][path[-1][1]]))]
    #                     if newEffort[0] < res[0]:
    #                         path.append(neighbor)
    #                         seen.add(neighbor)
    #                         Solution.backtrack(path, seen, newEffort, matrix, res)
    #                         seen.remove(neighbor)
    #                         path.pop()

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        matrix = heights
        rowCount = len(matrix)
        columnCount = len(matrix[0])

        if rowCount <= 1 and columnCount <= 1:
            return 0

        # 写成closure了，这样直接捕捉外面的matrix，不用传进去了
        def feasible(threshold: int) -> bool:
            # 能否最多耗费threshold力气，从起点走到终点
            queue = {(0, 0)} # 俗套的BFS
            traveled = set()

            while queue:
                levelQueue = set()

                for node in queue:
                    if node == (rowCount - 1, columnCount - 1):
                        # 如果已经走到终点了
                        return True # 说明可以花费不超过threshold的力气达成目标

                    (i, j) = node
                    neighbors = [
                        (i + 1, j),
                        (i, j + 1),
                        (i - 1, j),
                        (i, j - 1),
                    ]

                    for neighbor in neighbors:
                        if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount and neighbor not in traveled and neighbor not in levelQueue:
                            if abs(matrix[i][j] - matrix[neighbor[0]][neighbor[1]]) <= threshold:
                                # 力气够用，能从当前这一格爬到下一格
                                levelQueue.add(neighbor)

                    traveled.add(node)

                queue = levelQueue

            return False

        # 把f(n)当做0, 0, ..., 0, 1, 1, 1, ...这样的单调递增array，二分找到第一次出现1的位置
        target = True
        left = 0 # 有可能完全不费力
        right = max([
            abs(matrix[0][j] - matrix[0][j - 1])
            for j in range(1, columnCount)
        ] + [
            abs(matrix[i][0] - matrix[i - 1][0])
            for i in range(1, rowCount)
        ]) + 1 # 随便选一条路径，就选上右这条路径了，假设上右这条路径花费力气k，地图中一定存在一条花费力气小于等于k的路径

        while left < right:
            middle = (left + right) // 2
            test = feasible(middle) # 普通的二分是比较target和array[middle]，这里不过是把array[middle]换成了f(middle)而已，没什么区别
            if target > test:
                left = middle + 1
            elif target < test:
                right = middle
            else:
                right = middle

        return left

    # 总之就是没法用back track咯……
    # @staticmethod
    # def backtrack(path: List[int], seen: Set[Tuple[int, int]], threshold: int, matrix: List[List[int]], res: List[int]):
    #     if res[0] == True:
    #         return

    #     rowCount = len(matrix)
    #     columnCount = len(matrix[0])

    #     if len(path) == 0:
    #         path.append((0, 0))
    #         seen.add((0, 0))
    #         Solution.backtrack(path, seen, threshold, matrix, res)
    #         seen.remove((0, 0))
    #         path.pop()
    #     elif path[-1] == (rowCount - 1, columnCount - 1):
    #         res[0] = True
    #     else:
    #         (i, j) = path[-1]
    #         neighbors = [
    #             (i + 1, j),
    #             (i, j + 1),
    #             (i - 1, j),
    #             (i, j - 1),
    #         ]

    #         for neighbor in neighbors:
    #             if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount and neighbor not in path:
    #                 if abs(matrix[neighbor[0]][neighbor[1]] - matrix[i][j]) <= threshold:
    #                     path.append(neighbor)
    #                     seen.add(neighbor)
    #                     Solution.backtrack(path, seen, threshold, matrix, res)
    #                     seen.remove(neighbor)
    #                     path.pop()


s = Solution()
print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])) # 2
print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]])) # 1
print(s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])) # 0
