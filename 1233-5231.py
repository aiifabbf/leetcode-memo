"""
删掉所有的子目录

如果一个目录是另一个目录的子目录，就删掉它。

暴力做法就可以了。先把所有的目录从

::

    "/a/b/c/d"

的形式转换成

::

    ("a", "b", "c", "d")

这种形式。然后再按字典序从小到大排序。这样就可以形成树状结构，子目录永远会出现在这个子目录所属的主目录的后面。

::

    a
    a, b
    c, d
    c, d
    c, d, e
    c, f

对于每个目录，看这个目录的前缀是否已经见过，如果见过了，说明这个目录是一个子目录；如果没有见过，说明这个目录是一个主目录。
"""

from typing import *

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders = sorted(map(lambda v: tuple(v.split("/")[1: ]), folder)) # 先把每个目录从 ``"/a/b/c/d"`` 这种形式变成 ``("a", "b", "c", "d")`` 这种形式。然后按字典顺序排序。
        seen = set() # 存已经见过的主目录

        for folder in folders: # 遍历每个目录

            for i in range(1, len(folder)):
                if folder[: i] in seen: # 如果这个目录的某个前缀是主目录
                    break # 说明这个目录是某个主目录的子目录
            else: # 没有见过
                seen.add(folder) # 说明这个目录是主目录

        return list(map(lambda v: "/" + "/".join(v), seen)) # 把所有主目录变回 ``/a/b/c/d`` 的形式

s = Solution()
print(s.removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(s.removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"]))
print(s.removeSubfolders(folder = ["/a/b/c","/a/b/ca","/a/b/d"]))