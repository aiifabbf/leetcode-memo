"""
复制Node形式表示的图

我一开始想到的方法是用广度优先，先把Node形式表示的图转换成hash map形式表示的图，然后再转换回来。

后来一想好像不用这么麻烦，直接两次广度优先就好了

1.  第一次广度优先扫描的目的是把所有节点都挑出来

    给每个节点都生成一个对应的值相同的新节点对象，但暂时不关心有哪些节点和自己相邻。

2.  第二次广度优先扫描的目的是处理相邻节点的关系

    看旧节点周围有哪些相邻节点，然后把这些相邻节点对应的新节点对象接到旧节点对应的新节点上（好绕啊）。

简而言之就是

1.  第一遍广度优先，生成一个key是旧节点、value是新节点的hash map，也就是一个旧节点到新节点的映射
2.  第二遍广度优先，看旧节点周围有哪些节点，然后把这些节点对应的新节点从hash map里找出来，接到旧节点对应的新节点上

但这两种方法复杂度应该是一样的……
"""

from typing import *

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

import collections

class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        startNode = node # 保存一下起始节点
        oldNewMapping = {} # 旧节点到新节点的映射，key是旧节点，value是新节点
        queue = collections.deque([node]) # 俗套的广度优先啦
        traveled = set()

        while queue:
            length = len(queue)

            for _ in range(0, length):
                node = queue.popleft()
                oldNewMapping[node] = Node(node.val, []) # 给每个旧节点都生成一个值和旧节点完全相同的新节点，同时放到hash map里，但是不处理相邻节点之间的连接关系，留到第二次广度优先的时候再处理

                for neighbor in node.neighbors:
                    if neighbor not in traveled:
                        queue.append(neighbor)

                traveled.add(node)

        # 第一次广度优先结束了，下面开始第二次，目的是处理连接关系
        queue.clear() # 清空queue
        queue.append(startNode) # 加入起始节点，其实可以随便加入什么节点，反正只要是图里的某个节点就好了
        traveled.clear() # 清空已遍历过的节点集合

        while queue:
            length = len(queue)

            for _ in range(0, length):
                node = queue.popleft()
                oldNewMapping[node].neighbors = list(map(lambda n: oldNewMapping[n], node.neighbors)) # 处理相邻节点之间的连接关系，把旧节点的邻居统统通过hash map找到对应的新节点，组成一个list，变成当前节点对应的新节点的neighbors属性

                # 这里不需要多想一步，去把旧节点的neighbors列表里加上当前节点对应的新节点，因为遍历到那个节点的时候，自然而然就会加上的。遍历到每个节点的时候，只要关心好当前这个节点向外能到达哪些邻居节点就可以了，而无需关心邻居节点到达当前节点的事情。

                for neighbor in node.neighbors:
                    if neighbor not in traveled:
                        queue.append(neighbor)

                traveled.add(node)

        return oldNewMapping[startNode] # 返回初始节点对应的新节点

    # 第一次写的时候用的是先转换成关联集合、再转回来的方法。复杂度应该是一样的……
    # def cloneGraph(self, node: "Node") -> "Node":
    #     graph = self.nodeToGraph(node)
    #     return self.graphToNode(graph, node.val)

    def nodeToGraph(self, node: "Node") -> dict: # 把Node形式表示的图转换成关联列表表示的图
        if node:
            graph = {}
            queue = collections.deque([node])
            traveled = set()

            while queue:
                length = len(queue)

                for _ in range(0, length):
                    node = queue.popleft()
                    graph[node.val] = list(map(lambda n: n.val, node.neighbors))
                    queue.extend(filter(lambda n: n.val not in traveled, node.neighbors))
                    traveled.add(node.val)

            return graph
        else:
            return {}

    def graphToNode(self, graph: dict, start: int) -> "Node": # 把关联列表表示的图转换成Node形式表示的图
        valNodeMapping = {k: Node(k, []) for k in graph.keys()}
        queue = collections.deque([start])
        traveled = set()

        while queue:
            length = len(queue)

            for _ in range(0, length):
                val = queue.popleft()
                node = valNodeMapping[val]
                node.neighbors = list(map(lambda v: valNodeMapping[v], graph[val]))
                queue.extend(filter(lambda v: v not in traveled, graph[val]))
                traveled.add(val)

        return valNodeMapping[start]