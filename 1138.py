"""
给一张字母地图

::

    a b c d e
    f g h i j
    k l m n o
    p q r s t
    u v w x y
    z
      ^ ^ ^ ^---注意这几个位置不可达

一个机器人可以在这个地图上上下左右走，到达某个字母的上面可以落笔，记下当前这个字母。

机器人一开始在 ``(0, 0)`` ，``U, D, L, R`` 分别表示上下左右移动一格， ``!`` 表示落笔。

现在给一个字符串，问机器人的最少移动次数的动作历史，包括移动和落笔。

比如要形成 ``abc`` ，机器人的动作历史是 ``!R!R!`` 。

没什么难的。只是要注意好 ``z`` 的右边是不可达的，所以从 ``z`` 出发的轨迹要特殊处理（先上下移动、再左右移动以免触碰到不可达区域），到 ``z`` 的轨迹也要特殊处理（先左右移动、再上下移动）。
"""

from typing import *

import string

class Solution:
    valuePositionMapping = {v: ((ord(v) - ord("a")) // 5, (ord(v) - ord("a")) % 5) for v in string.ascii_lowercase} # 字母和字母位置的对应关系，方便快速查询

    def alphabetBoardPath(self, target: str) -> str:
        res = []
        lastPosition = (0, 0)

        for v in target:
            position = self.valuePositionMapping[v]
            if v == "z": # 目标是z
                if position[1] > lastPosition[1]: # 先左右移动
                    res.append("R" * (position[1] - lastPosition[1]))
                if position[1] < lastPosition[1]:
                    res.append("L" * (lastPosition[1] - position[1]))
                if position[0] > lastPosition[0]: # 再上下移动
                    res.append("D" * (position[0] - lastPosition[0]))
                if position[0] < lastPosition[0]:
                    res.append("U" * (lastPosition[0] - position[0]))
            else: # 因为本来默认就是先上下移动再左右移动，所以从z出发的情况不用特殊处理
                if position[0] > lastPosition[0]:
                    res.append("D" * (position[0] - lastPosition[0]))
                if position[0] < lastPosition[0]:
                    res.append("U" * (lastPosition[0] - position[0]))
                if position[1] > lastPosition[1]:
                    res.append("R" * (position[1] - lastPosition[1]))
                if position[1] < lastPosition[1]:
                    res.append("L" * (lastPosition[1] - position[1]))
            res.append("!") # 落笔
            lastPosition = position

        return "".join(res)

# s = Solution()
# print(s.valuePositionMapping)
# print(s.alphabetBoardPath("l"))
# print(s.alphabetBoardPath("leet"))
# print(s.alphabetBoardPath("code"))
# print(s.alphabetBoardPath("zdz"))