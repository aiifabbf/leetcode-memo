from typing import *

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # 一改：终止条件不对。
        # 二改：终止条件还是不对。

        # 一开始想的是用双指针一点一点来搞，但是状态转移条件一直搞不对，所以干脆算了，直接先把两个字符串砍成一块一块，每一块里的字符串都一样，比如 ``aaleex`` 砍成 ``["aa", "l", "ee", "x]"``，如果两个字符串砍成的肉块数目不一样，直接false；如果数目一样，但是发现某一组肉块的成分不一样，直接false；如果某一组肉块的成分一样，但是name那边的肉块分量大一点，直接false。
        buffer = [name[0]]
        for i in range(1, len(name)):
            if name[i] == buffer[-1][-1]:
                buffer[-1] = buffer[-1] + name[i]
            else:
                buffer.append(name[i])
        name = buffer

        buffer = [typed[0]]
        for i in range(1, len(typed)):
            if typed[i] == buffer[-1][-1]:
                buffer[-1] = buffer[-1] + typed[i]
            else:
                buffer.append(typed[i])
        typed = buffer

        if len(name) != len(typed):
            return False
        
        for i in range(0, len(name)):
            if name[i][0] != typed[i][0]:
                return False
            elif len(name[i]) > len(typed[i]):
                return False
        
        return True

s = Solution()
assert s.isLongPressedName("alex", "aaleex")
assert not s.isLongPressedName("saeed", "ssaaedd")
assert s.isLongPressedName("leelee", "lleeelee")
assert s.isLongPressedName("laiden", "laiden")
assert not s.isLongPressedName("pyplrz", "ppyypllr")
assert not s.isLongPressedName("kikcxmvzi", "kiikcxxmmvvzz")
assert s.isLongPressedName("vtkgn", "vttkgnn")