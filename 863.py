"""
给一个二叉树、一个其中的节点、一个距离K，找到这个二叉树里距离这个节点为K的所有节点的值。

用图的广度优先搜索很简单，先把树转换成用hash map表示的图，再广度优先搜索就可以了。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections # 广度优先搜索会用到queue，collections里的deque是queue的高效实现

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if root:
            graph = {} # 用dict来存图
            queue = collections.deque([root])

            while queue:
                size = len(queue)

                for _ in range(0, size):
                    v = queue.popleft()
                    if v.left:
                        queue.append(v.left)
                        graph[v.val] = graph.get(v.val, set()).union({v.left.val}) # 把这个节点和左节点的连接记录在graph里面
                        graph[v.left.val] = graph.get(v.left.val, set()).union({v.val}) # 因为是无向图，所以左节点和当前节点的连接也要记录一遍，虽然重复了
                    if v.right:
                        queue.append(v.right)
                        graph[v.val] = graph.get(v.val, set()).union({v.right.val}) # 右节点同理
                        graph[v.right.val] = graph.get(v.right.val, set()).union({v.val})

            # 到这里，就完成了树到图的转换了。下面就是图的广度优先搜索了

            queue = collections.deque([target.val]) # 下面待遍历的节点
            traveled = set() # 已遍历过的节点
            distance = 0

            while len(queue) != 0 and distance < K:
                # 此时queue里就是距离target为distance的所有节点
                length = len(queue)

                for _ in range(0, length):
                    v = queue.popleft()
                    queue.extend(filter(lambda v: v not in traveled, graph.get(v, set())))
                    traveled.add(v)

                distance += 1

            return list(queue)

        else:
            return []