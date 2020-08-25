"""
.. default-role:: math

给一个字母矩阵，问有没有环

比如给个

::

    a a a a
    a b b a
    a b b a
    a a a a

外圈的 ``a`` 能凑成一个环、内圈的 ``b`` 也能凑成一个环。

严谨一点说，就是能不能找到一个字母，以它为起点，沿着上下左右相同字母的路径走下去，最后回到起点。这其实是DFS的思路。

等效的BFS说法是，以它为起点，沿着不同的路径走下去，最后能碰面。碰面的意思是在某个时刻，会发现将要放入queue的neighbor早就已经在queue里面了。这个neighbor肯定是走另一条路的另一个node放进去的。

所以如果有环的话，你从左上角开始BFS，最终一定会在右下角的某个位置发现即将放入queue的元素已经在queue里面了。比如

::

    a a a a
    a b b a
    a b b a <- 0
    a a a a <- 2
        ^
        |
        1

假设从左上角的 ``a`` 开始BFS，BFS到下面的时候，1这个 ``a`` 在把2放入queue的时候发现2已经在queue里了，是因为走另外一条路的0已经把2放到队列里了。
"""


from typing import *


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rowCount = len(grid)
        columnCount = len(grid[0])
        traveled = set()  # 已经遍历过的节点

        for rowIndex in range(rowCount):  # 试着以每个节点为起点BFS
            for columnIndex in range(columnCount):
                position = (rowIndex, columnIndex)
                if position not in traveled:  # 当然不用以每个节点为起点都来一遍BFS，你从左上角出发、最后走到右下角，和从右上角出发、走到左下角是一样的，都在同一个环上。所以如果发现已经BFS过，就不需要再来一遍了，上一次以其他节点为起点的BFS肯定已经搜索过你了
                    queue = [position]

                    while queue:
                        levelQueue = []

                        for node in queue:
                            neighbors = [
                                (node[0] - 1, node[1]),
                                (node[0] + 1, node[1]),
                                (node[0], node[1] - 1),
                                (node[0], node[1] + 1)
                            ]

                            for neighbor in neighbors:
                                if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount:
                                    if neighbor in levelQueue: # bingo，发现这个neighbor居然已经在queue里面了。如果没有环的话，这个neighbor只能由我放入queue，不可能被别人放到queue里。唯一的可能就是这是走另一条路径的节点放的
                                        return True # 所以遇到了环
                                    if neighbor not in traveled and grid[neighbor[0]][neighbor[1]] == grid[node[0]][node[1]]:
                                        levelQueue.append(neighbor)

                            traveled.add(node)

                        queue = levelQueue

        return False


s = Solution()
print(s.containsCycle([["a", "a", "a", "a"], ["a", "b", "b", "a"], [
      "a", "b", "b", "a"], ["a", "a", "a", "a"]]))
print(s.containsCycle([["c", "c", "c", "a"], ["c", "d", "c", "c"], [
      "c", "c", "e", "c"], ["f", "c", "c", "c"]]))
print(s.containsCycle([["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))
