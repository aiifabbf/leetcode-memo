"""
判断数独盘上的数字是否符合数独的规则

数独的三条规则

-   每行不能出现两个重复数字
-   每列不能出现两个重复数字
-   每宫不能出现两个重复数字

    把9x9的数独盘切成9个3x3的小区域，这些小区域就是宫。
"""

from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # for rowIndex, row in enumerate(board): # 检查每行是否有重复数字
        #     numbersInThisRow = set()

        #     for columnIndex, box in enumerate(row):
        #         if box == ".":
        #             continue
        #         else:
        #             if box in numbersInThisRow:
        #                 return False # 这行出现了重复数字
        #             else:
        #                 numbersInThisRow.add(box)

        # for columnIndex in range(9): # 检查每列是否有重复数字
        #     numbersInThisColumn = set()

        #     for rowIndex in range(9):
        #         box = board[rowIndex][columnIndex]
        #         if box == ".":
        #             continue
        #         else:
        #             if box in numbersInThisColumn:
        #                 return False # 这列出现了重复数字
        #             else:
        #                 numbersInThisColumn.add(box)

        # subBoxes = [
        #     (0, 0),
        #     (0, 3),
        #     (0, 6),
        #     (3, 0),
        #     (3, 3),
        #     (3, 6),
        #     (6, 0),
        #     (6, 3),
        #     (6, 6)
        # ] # 每宫的左上角的位置

        # for subbox in subBoxes: # 检查每宫里是否含有重复数字
        #     indexes = [(i + subbox[0], j + subbox[1]) for i in range(3) for j in range(3)] # 这一宫里所有数字的位置
        #     boxes = filter(lambda v: v != ".", map(lambda w: board[w[0]][w[1]], indexes))
        #     numbersInThisSubbox = set()

        #     for box in boxes:
        #         if box in numbersInThisSubbox:
        #             return False # 这一宫里出现了重复数字
        #         else:
        #             numbersInThisSubbox.add(box)

        # return True

        # 看排名还看到了只遍历一次的神仙做法，大致思路是用3个set，分别专门用来判断行重复、列重复和宫重复。

        # 但是速度和上面遍历3次的没差别……可能是python overhead的问题吧

        seenInRow = set() # 专门用来判断行重复的set，里面存行号、数字对
        seenInColumn = set() # 存列号、数字对
        seenInSubbox = set() # 存宫号、数字对

        for rowIndex, row in enumerate(board):

            for columnIndex, box in enumerate(row):
                if box != ".":

                    for v, s in zip([(rowIndex, box), (columnIndex, box), (rowIndex // 3, columnIndex // 3, box)], [seenInRow, seenInColumn, seenInSubbox]):
                        if v in s:
                            return False
                        else:
                            s.add(v)

        return True

# s = Solution()
# print(s.isValidSudoku([
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ])) # true
# print(s.isValidSudoku([
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ])) # false