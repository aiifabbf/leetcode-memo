"""
给一些地理元素的从属关系，比如“地球包含北美洲和南美洲”、“北美洲包含美国和加拿大”，再给两个地理元素，问能包含这两个地理元素的最小单元是什么。

比如给

-   地球包含北美洲和南美洲
-   北美洲包含美国和加拿大
-   美国包含纽约和波士顿
-   加拿大包含渥太华魁北克
-   南美洲包含巴西

然后给你“魁北克”和“纽约”，问能包括魁北克和纽约的最小单元是什么。当然是北美洲。为什么？因为

魁北克的从属链是

1.  魁北克
2.  加拿大
3.  北美洲
4.  地球

纽约的从属链是

1.  纽约
2.  美国
3.  北美洲
4.  地球

也就是要找到从属链上最近的分叉点。类似做一次diff，找到有差别的第一行。

那就先想办法把从属链搞出来、然后diff。
"""

from typing import *

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        mapping = {} # key是地理单元，value是这个地理单元的parent。和一般树的表示方法不同，这里是子节点指向父节点

        for region in regions:
            root = region[0]
            if root not in mapping: # 如果树里面没有这个节点
                mapping[root] = root # 创建一个节点，并且认为自己是根节点

            for subregion in region[1: ]: # 让下面所有的从属节点都指向自己
                mapping[subregion] = root

        root = region1
        roots1 = [region1] # region1的从属链

        while root != mapping[root]:
            roots1.append(mapping[root])
            root = mapping[root]

        roots1.reverse() # 倒过来就是从大范围到小范围

        root = region2
        roots2 = [region2] # region2的从属链

        while root != mapping[root]:
            roots2.append(mapping[root])
            root = mapping[root]

        roots2.reverse() # 武汉-湖北-中国变成中国-湖北-武汉

        # diff，找到开始分叉的第一个节点
        for i in range(min(len(roots1), len(roots2))):
            if roots1[i] != roots2[i]: # 发现开始分叉了
                return roots1[i - 1] # 那么刚才那个就是分叉点
        else: # 根本没有找到分叉点。这种情况是有可能的，比如给中国-湖北、中国-湖北-武汉，这时候答案应该是湖北。也就是短的那个的最后一个节点。
            if len(roots1) > len(roots2):
                return roots2[-1]
            elif len(roots1) < len(roots2):
                return roots1[-1]
            else:
                return roots1[-1]

s = Solution()
print(s.findSmallestRegion(regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York")) # north america

print(s.findSmallestRegion([["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]],
"Canada",
"Quebec")) # canada

print(s.findSmallestRegion([["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]],
"Canada",
"South America")) # earth