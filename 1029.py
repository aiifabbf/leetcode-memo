r"""
有一个点集 :math:`\{(a_i, b_i)\}` 其中一共有2n个点，现在要取n个点，取它们的 :math:`a_i` 值全部累加起来，再把剩下的n个点的 :math:`b_i` 值全部累加起来。问这个和最小是多少。

原问题用了一个挺好的背景：总共有2n个人要onsite面试，其中n个人去A城市面试、剩下的n个人去B城市面试，每个人去A城市的花费是 :math:`a_i` 、去B城市的花费是 :math:`b_i` ，为了节省开支，公司应该怎样安排。

其实就是一个很简单的排序问题，定性分析就是，如果一个人去A城市花费的成本比让他去B城市的花费低非常非常多，我们当然是想尽可能安排他去A城市的；并且我们发现我们其实只关心去A城市和去B城市的花费的绝对差值，而不关心去A城市或者去B城市的绝对花费，因为再贵也要安排他面试。总结一下

-   一个人去A城市的花费比去B城市的花费相比越小，我们越希望他去A城市
-   去A城市还是B城市，与去A城市或者B城市的绝对花费无关

所以本质上这个问题就是一个点集的排序问题，关键问题是目标函数的选取。这里目标函数应该选择去A城市的花费和去B城市的花费的差值。然后从小到大排序，第1个元素显然就是去A城市比去B城市便宜最多的人，所以当然应该让他去A城市；最后一个元素显然就是去A城市比去B城市亏最多的人，所以当然应该让他去B城市。取前n个人去A城市、取最后n个人去B城市
"""

from typing import *

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        sortedCosts = sorted(costs, key=lambda x: x[0] - x[1]) # 按去A城市和去B城市的花费的差值来从小到大排序
        a = map(lambda x: x[0], sortedCosts[: length // 2]) # 前n个人去A城市
        b = map(lambda x: x[1], sortedCosts[length // 2: ]) # 后n个人去B城市
        return sum(a) + sum(b)

# s = Solution()
# print(s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])) # 110
# print(s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])) # 1859