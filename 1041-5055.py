"""
给一串指令

-   走一格
-   左转
-   右转

问无限循环这串指令，机器人的路径是否有界。

其实本质上就是问执行一次这串指令之后，机器人是不是头朝上并且不在原点。如果执行过后，机器人头朝上、并且不在原点，那么机器人的路径一定无界。

我还不会证明这个。
"""

from typing import *

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        front = "up" # 一开始机器人头朝上
        position = [0, 0] # 一开始机器人在原点

        for instruction in instructions: # 一条一条执行指令
            if instruction == "G":
                if front == "up":
                    position[1] += 1
                elif front == "down":
                    position[1] -= 1
                elif front == "left":
                    position[0] -= 1
                else:
                    position[0] += 1
            elif instruction == "L":
                if front == "up":
                    front = "left"
                elif front == "down":
                    front = "right"
                elif front == "left":
                    front = "down"
                else:
                    front = "up"
            elif instruction == "R":
                if front == "up":
                    front = "right"
                elif front == "down":
                    front = "left"
                elif front == "right":
                    front = "down"
                else:
                    front = "up"

        if front == "up" and position != [0, 0]: # 如果最后机器人头朝上、并且不在原点，那么无限循环这串指令，机器人的路径一定无界
            return False
        else:
            return True

# s = Solution()
# assert s.isRobotBounded("GGLLGG") == True
# assert s.isRobotBounded("GG") == False
# assert s.isRobotBounded("GL") == True
# assert s.isRobotBounded("LLLRLLLRLLGLLGGRGLLLGGLRRRRRGLRLRLRLGGRGRGRLLLLLLGLLRLGLGLRLGGGRR") == False
# assert s.isRobotBounded("GGRGGRGGRGGR") == True
# assert s.isRobotBounded("RLLGLRRRRGGRRRGLLRRR") == True