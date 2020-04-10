"""
验证某个先根遍历是否是一个二分搜索树的先根遍历路径。

.. 这题居然要氪金……

这题真的很难，我看了一圈discussion都没看懂，最后自己想了一个插槽的办法。看图比较容易理解，博客里有 `配图 <http://aiifabbf.github.io/posts/mathworks-interview/index.html#id2>`_ 和详细解释。
"""

from typing import *

# class Solution:
#     def verifyPreorder(self, preorder: List[int]) -> bool:
#         if preorder:
#             root = preorder[0]
#             rightTreeIndex = -1

#             for i, v in enumerate(preorder[1: ], 1):
#                 if v >= root:
#                     rightTreeIndex = i
#                     break
#             else:
#                 return self.verifyPreorder(preorder[1: ])

#             for v in preorder[rightTreeIndex: ]:
#                 if v < root:
#                     return False
#             else:
#                 return self.verifyPreorder(preorder[rightTreeIndex: ]) and self.verifyPreorder(preorder[1: rightTreeIndex])

#         else:
#             return True
# 这样可以做，但是实在是太慢了

# 我自己的做法
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = [(float("-inf"), float("inf"))] # 第一个数字当然只能插入到根节点的位置。而且因为现在BST里面还没有元素，所以第一个插槽的范围是(-inf, inf)

        for v in preorder: # 开始重建BST，尝试插入preorder中的每个数字

            while len(stack) != 0 and stack[-1][1] < v: # 检测stack顶端的插槽能否放入当前数字
                stack.pop() # 如果不能放入当前数字，就直接扔掉这个插槽，因为反正之后的数字也没法放进去

            if len(stack) != 0 and stack[-1][0] < v < stack[-1][1]: # 数字可以放入某个插槽
                interval = stack.pop() # 把数字填入这个插槽
                stack.append((v, interval[1])) # 填入数字之后，又产生了两个新的可用插槽。也可以理解为把刚才的插槽分解成了两个插槽
                stack.append((interval[0], v))
            else: # 说明stack空了，没有找到任何一个插槽能放下当前数字
                return False # BST重建失败

        return True # 重建成功，每个数字都放入了BST中正确的位置

# leetcode某个discussion的做法，我不懂
# class Solution:
#     def verifyPreorder(self, preorder: List[int]) -> bool:
#         stack = []
#         lower = float("-inf")

#         for v in preorder:

#             while len(stack) != 0 and stack[-1] < v:
#                 lower = stack.pop()

#             if v < lower:
#                 return False
#             else:
#                 stack.append(v)

#         return True

# tzb的做法，我不懂。感觉和discussion的做法差不多
# class Solution:
#     def verifyPreorder(self, preorder: List[int]) -> bool:
#         stack = []
#         isBST = True
#         root = float("-inf")

#         for v in preorder:
#             if v < root:
#                 isBST = False
#                 break
        
#             while len(stack) != 0 and v > stack[-1]:
#                 root = stack.pop()

#             stack.append(v)

#         return isBST

s = Solution()
print(s.verifyPreorder([5, 2, 6, 1, 3])) # false
print(s.verifyPreorder([5, 2, 1, 3, 6])) # true
print(s.verifyPreorder([10, 7, 4, 8, 6, 40, 23])) # false