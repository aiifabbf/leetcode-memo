"""
一个坏橘子下一秒会腐蚀掉上下左右相邻的好橘子，问多久之后整个箱子里全是坏橘子？也有可能有一些橘子与世隔绝所以永远不坏，这时返回-1。

典型的图的广度优先搜索。
"""

# 想到了元胞自动机

from typing import *

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set() # 存放坏橘子的位置
        oranges = set() # 存放所有橘子的位置

        for rowIndex, row  in enumerate(grid): # 遍历一遍，把rotten和oranges这两个集合建立起来
            
            for columnIndex, box in enumerate(row):
                position = (rowIndex, columnIndex)
                if box == 2: # 如果是个坏橘子
                    rotten.add(position)
                if box != 0: # 如果是个橘子
                    oranges.add(position)

        time = 0
        newRotten = set() # 下一秒从好橘子变成坏橘子的橘子

        while True:
            newRotten.clear()

            for position in rotten: # 遍历所有的坏橘子
                neighbors = [
                    (position[0] - 1, position[1]),
                    (position[0] + 1, position[1]),
                    (position[0], position[1] - 1),
                    (position[0], position[1] + 1)
                ] # 坏橘子的上下左右

                for neighbor in neighbors:
                    if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 1: # 如果上下左右邻近的地方有好橘子
                        newRotten.add(neighbor) # 标记成下一秒会变成坏橘子的橘子
                        grid[neighbor[0]][neighbor[1]] = 2 # 变成坏橘子
            
            if newRotten: # 说明下一秒有橘子会变坏
                time = time + 1
                rotten.update(newRotten)
            else: # 说明下一秒没有橘子变坏，这时候有两种情况
                if len(oranges) == len(rotten): # 所有橘子都已经变坏了，所以也没橘子可以再腐蚀了
                    return time
                else: # 有一些橘子与世隔离，永远不变坏
                    return -1

# s = Solution()
# print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
# print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
# print(s.orangesRotting([[0, 2]])) # 0