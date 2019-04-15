"""
给两个矩形的左下角、右上角端点坐标，判断这两个矩形是否有重合。

两个矩形都是开集，边界不算矩形，所以如果两个矩形只是边重合，不算重合。

重合的条件挺难描述的，但是不重合的条件很容易描述，又因为两个矩形只可能要么重合、要么不重合，所以把不重合的条件反一反就是重合了。

两个矩形不重合的充分必要条件是

-   其中一个矩形的左下角顶点永远在另一个矩形的右上角顶点的右边或者上边
-   或者，其中一个矩形的右上角顶点永远在另一个矩形的左下角顶点的左边或者下边
"""

from typing import *

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1BottomLeft = rec1[0: 2]
        rec1TopRight = rec1[2: ]
        rec2BottomLeft = rec2[0: 2]
        rec2TopRight = rec2[2: ]
        if rec2BottomLeft[0] >= rec1TopRight[0] or rec2BottomLeft[1] >= rec1TopRight[1]: # 其中一个矩形的左下角顶点在另一个矩形的右上角顶点的右边或者上边
            return False
        elif rec2TopRight[0] <= rec1BottomLeft[0] or rec2TopRight[1] <= rec1BottomLeft[1]: # 其中一个矩形的右上角顶点在另一个矩形的左下角顶点的左边或者下边
            return False
        else: # 其他情况一律都是重合的
            return True

# s = Solution()
# assert s.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]) == True
# assert s.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]) == False