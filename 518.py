"""
.. default-role:: math

凑硬币。给一组面值，每种面值可以用无限次，问总共有多少种凑法。重复的不算。

比如给1、2、5面值，要凑到5，总共有

::

    5
    2 2 1
    2 1 1 1
    1 1 1 1 1

一共4种凑法。

::

    2 2 1
    2 1 2
    1 2 2

这几种都算重复的，只能算一种凑法。

这一题今天（2019/10/14）算法课lab的时候提到了，终于学会怎么做了，居然又是动态规划。

设 ``dp[amount][i]`` 是用 ``coins[0], coins[1], ..., coins[i]`` 凑出数额 ``amount`` 的组合种类。思考一下 ``dp[amount][i]`` 和前面的项有什么关系

-   可以完全不用 ``coins[i]`` （也就是用0个 ``coins[i]`` ），只用前面 `i` 个硬币 ``coins[0], coins[1], ..., coins[i - 1]`` 凑出 ``amount``
-   可以用1个 ``coins[i]`` 、再用前面的 `i` 个硬币 ``coins[0], coins[1], ..., coins[i - 1]`` 凑出 ``amount - coins[i]``
-   可以用2个 ``coins[i]`` 、再用前面的 `i` 个硬币 ``coins[0], coins[1], ..., coins[i - 1]`` 凑出 ``amount - 2 * coins[i]``
-   ...
-   可以用 `q` 个 ``coins[i]`` 、再用前面的 `i` 个硬币 ``coins[0], coins[1], ..., coins[i - 1]`` 凑出 ``amount - q * coins[i]`` ，当然前提是 ``amount - q * coins[i] >= 0``

为什么这样子可以保证不出现重复情况呢？因为在用前面 `i` 个硬币 ``coins[0], coins[1], ..., coins[i - 1]`` 的时候， ``coins[i]`` 是没有用到的，我们人为强行指定了每次要用多少个 ``coins[i]`` ，所以不会出现重复的情况。

顺便提一下我觉得这道题用递归写、而不是用迭代写有两个好处

-   写起来更容易

    其实这一题里挺难把递归转化成迭代的

-   有些表项是不用填的、永远碰不到的

    这样可以省很多时间和空间。
"""

from typing import *

import math

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    #     if amount == 0:
    #         return 1
    #     elif amount < 0:
    #         return 0
    #     else:
    #         # print(self.allCombinations(amount, coins))
    #         return len(self.allCombinations(amount, tuple(sorted(coins))))

    # @functools.lru_cache(None)
    # def allCombinations(self, amount: int, coins: List[int]) -> set:
    #     if amount <= 0:
    #         return set()
    #     else:
    #         combinations = set()

    #         for v in filter(lambda v: v <= amount, coins):
    #             if v == amount:
    #                 combinations.add((v, ))
    #             elif v < amount:
    #                 paths = self.allCombinations(amount - v, tuple(w for w in coins if w <= amount - v))
    #                 combinations.update(tuple(sorted(path + (v, ))) for path in paths)
    #             else:
    #                 continue

    #         return combinations
    # 暴力不可取

        # 先处理两个corner case
        if len(coins) == 0 and amount == 0: # 没有硬币可用、数额也正好是0
            return 1
        elif len(coins) == 0 and amount != 0: # 没有硬币可用、同时数额不是0
            return 0 # 没有办法

        dp = {} # 相当于一个cache，避免重复计算

        def opt(amount: int, index: int) -> int: # 递推式
            if (amount, index) in dp: # 如果发现之前计算过了
                return dp[amount, index] # 就不要重复计算了，直接返回结果吧
            else: # 如果发现之前没有计算过
                if index == 0: # 初始条件，只用第一种硬币凑出数额
                    if amount % coins[index] == 0: # 如果发现数额可以被第一种硬币整除
                        res = 1 # 恭喜，找到了1种组合方法
                    else: # 不能被硬币整除
                        res = 0 # 那就没办法了
                else: # index > 0的时候，需要用递推式了
                    t = 0 # 用多少个coins[index]
                    res = 0

                    while True:
                        if amount - t * coins[index] >= 0: # 要保证数额不小于0
                            res += opt(amount - t * coins[index], index - 1)
                            t += 1 # 试试多用一个coins[index]
                        else: # 一旦发现数额小于0了
                            break # 就不要再算下去了，没有意义了
                    
                    # 当然也可以用下面这种写法
                    # res = sum(opt(amount - t * coins[index], index - 1) for t in range(0, math.floor(amount / coins[index]) + 1))

                dp[amount, index] = res # 计算结果加入cache
                return res

        res = opt(amount, len(coins) - 1) # 原问题的答案是dp[amount][len(coins) - 1]
        return res

# s = Solution()
# print(s.change(5, [1, 2, 5])) # 4
# print(s.change(3, [2])) # 0
# print(s.change(0, [])) # 1
# print(s.change(300, [1, 2, 5])) # 4621