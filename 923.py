r"""
找到array里所有满足 `a_i + a_j + a_k = t` 的 `(i, j, k), i < j < k` 的总个数。

3sum的变体，3sum只是要求找到一个 `(i, j, k)` 就可以了，这里是要找到所有满足条件 `(i, j, k)` 的个数。如果直接用3sum来做，复杂度是 `O(n^2)` 。

因为只是要得到符合条件的 `(i, j, k)` 的个数，所以可以做一些优化，首先我们不去求符合条件的 `(i, j, k)` ，而是去求符合条件的 `(a_i, a_j, a_k)` 以及它们出现的次数。这样对于含有巨量重复元素的array就能省很多时间。

和3sum一样，也是先写2sum，凑成 `a_j + a_k = t - a_i` ，然后外面再套一层。

这边我没有让处理2sum的函数直接接受一个array，而是让它接受一个 ``dict`` 存储的直方图作为参数，这样在array中含有大量重复元素的时候能节省时间。注意要处理 `a + a = t` 的情况、也就是 `a = b` 的情况。

这样一来，在外层的3sum也要对

-   `a = b = c`
-   `a = b \neq c`

这两种情况做特殊处理。
"""

from typing import *

import collections

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        counter = collections.Counter(A) # 先做出A的直方图，统计出A里面每个元素出现的次数，这样如果A里面含有非常非常多的重复元素就可以省很多时间
        res = collections.Counter() # 用来存(a, b, c)和它们出现的次数。怕麻烦，规定a <= b <= c

        for a in counter.keys():
            if 3 * a == target: # a == b == c的情况
                n = counter[a] # a出现的次数
                res[(a, a, a)] += n * (n - 1) * (n - 2) // 6 # 满足a + a + a == target的(a, a, a)出现的次数是C_n^3
            elif target - 2 * a in counter: # a == b != c的情况
                n = counter[a]
                cTimes = counter[target - 2 * a]
                res[tuple(sorted((a, a, target - a)))] += cTimes * n * (n - 1) // 2 # 从n个a中任意取出2个a、和一个c配对，使得a + a + c == target，所以满足条件的(a, a, c)出现的次数是C_n^2乘上c出现的次数

            # 其他情况
            # 为什么这边不是else呢，因为即使存在3 * a == target的情况，也不能保证后面不会出现a + b + c == target存在，所以这里不是else。
            aTimes = counter[a] # a出现的次数
            counter[a] = 0 # 需要把counter传给下层的2sum来处理，所以需要先把a出现的次数抹掉
            bcCounter = self.twoSumCounter(+counter, target - a) # 2sum得到满足b + c == target - a的(b, c)和它们出现的次数

            for k, v in bcCounter.items(): # k是满足b + c == target - a的(b, c)，v是这对(b, c)在后面出现的次数
                res[tuple(sorted((a, *k)))] += aTimes * v # 任意选取某个满足条件的(b, c)和前面的a配对，使得a + b + c == target，所以满足条件的(a, b, c)出现的次数就是a出现的次数乘上满足target - a == b + c的(b, c)出现的次数

        return sum(res.values()) % (10**9 + 7)

    def twoSumCounter(self, counter: "Dict", target: int) -> "Dict": # two sum
        seen = collections.Counter() # 每个值出现的次数
        res = collections.Counter() # 每个满足a + b = target的(a, b)出现的次数，怕麻烦，规定a <= b

        for v in counter.keys():
            if target - v in seen: # 处理a != b的情况
                res[tuple(sorted((target - v, v)))] += seen[target - v] * counter[v] # 可以任意取后面出现的某个b和前面出现的某个a配对加和形成target，所以b出现的次数乘以前面的a出现的次数就是(a, b)出现的次数
            if 2 * v == target: # 处理a == b的情况。这是和一般的2sum不一样的地方
                res[(v, v)] += counter[v] * (counter[v] - 1) // 2 # a内部配对，可以任意从n个a中选取2个配对，使得a + a == target，所以满足a + a = target的(a, a)出现的次数是C_n^2
            seen[v] = counter[v]

        return res

# s = Solution()
# print(s.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)) # 20
# print(s.threeSumMulti([0, 0, 0], 0)) # 1