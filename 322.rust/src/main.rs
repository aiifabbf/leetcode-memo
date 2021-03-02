/*
.. default-role:: math

给一些硬币，面值分别是 ``coins[0], coins[1], ...`` ，每种面值的硬币有无限多个，要用这些硬币凑成 `C` 元钱，最少需要多少个硬币？如果凑不出，返回-1。

学了背包问题之后大呼过瘾，马上定义 `f(j, c)` ，表示用 ``coins[0..j]`` 里的面值（用前 `j` 种面值的硬币）凑出 `c` 元钱最少需要多少个硬币。

递推式也能很快想到。多出一种面值 ``coins[j - 1]`` 有什么影响？

-   可以完全不用这种面值的硬币，或者说用0个面值是 ``coins[j - 1]`` 的硬币，那么 `f(j, c) = f(j - 1, c)`
-   可以用1个，那么剩下需要凑的钱只有 `c - a_{j - 1}` 元钱了， `f(j, c) = 1 + f(j - 1, c - a_{j - 1})`
-   可以用2个，剩下需要凑的钱有 `c - 2 a_{j - 1}` 元， `f(j, c) = 2 + f(j - 1, c - 2 a_{j - 1})`
-   ...
-   可以用 `k` 个，剩下需要凑的钱是 `c - k a_{j - 1}` 元， `f(j, c) = k + f(j - 1, c - k a_{j - 1})`

只要保证 `c - k a_{j - 1} \geq 0` 就可以了。所以递推式是

.. math::

    f(j, c) = \min\{ k + f(j - 1, c - k a_{j - 1}) | k \geq 0, c - k a_{j - 1} \geq 0 \}

复杂度大概是 `O(n^2 C)` 吧（我也不确定），是伪多项式阶的，而且有个 `n^2` ，所以挺慢的。

为什么有个 `n^2` ？因为表格本身是2维的，所以有 `O(nC)` 个格子，为了填充每个格子，还需要遍历 `c / a_{j - 1}` 次。

-----

另一种方法非常妙，忽略 `j` ，直接定义 `f(c)` 为凑出 `c` 元钱所需的最少硬币数量。递推式稍微难想一点。因为硬币都是一个一个攒出来的，所以

-   如果这 `c` 元钱里有1个面值为 `a_0` 的硬币，那么 `f(c) = 1 + f(c - a_0)`
-   如果有1个面值为 `a_1` 的硬币，那么 `f(c) = 1 + f(c - a_1)`
-   ...
-   如果有1个面值为 `a_i` 的硬币，那么 `f(c) = 1 + f(c - a_i)`

.. math::

    f(c) = \min\{ 1 + f(c - a_i) | c - a_i \geq 0 \}

复杂度仍然是 `O(nC)` ，比刚才的方法快多了。
*/

struct Solution;

impl Solution {
    #[cfg(feature = "knapsack")]
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut dp = vec![vec![std::i32::MAX; amount as usize + 1]; coins.len() + 1]; // dp[j][c] = 用coins[..j]里的硬币凑成c元钱的最少硬币数量。为了方便，暂时用inf表示凑不出的情况
        dp[0][0] = 0; // 初始条件，用前0种面值凑出0元钱，需要0个硬币

        for j in 1..=coins.len() {
            for c in 0..=amount as usize {
                for n in 0..=c / coins[j - 1] as usize {
                    let remain = dp[j - 1][c - n * coins[j - 1] as usize];
                    dp[j][c] = dp[j][c].min((n as i32).saturating_add(remain));
                }
            }
        }

        let res = dp[coins.len()][amount as usize];
        if res != std::i32::MAX {
            res
        } else {
            -1
        }
    }

    #[cfg(feature = "dp")]
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut coins = coins;
        coins.sort(); // 排序之后复杂度不变，不过实际上会快一点，因为后面用到了take_while，可以early break
        let mut dp = vec![std::i32::MAX; amount as usize + 1]; // dp[c] = 凑成c元钱的最少硬币数量
        dp[0] = 0; // 初始条件，凑成0元钱最少需要0个硬币

        for c in 1..=amount as usize {
            // for coin in coins.iter().cloned() {
            //     if c >= coin as usize {
            //         dp[c] = dp[c].min(dp[c - coin as usize].saturating_add(1));
            //     } else {
            //         break;
            //     }
            // }
            // 可以写成函数式
            dp[c] = coins
                .iter()
                .cloned()
                .take_while(|coin| c >= (*coin as usize)) // 要保证c - coins[i] >= 0，如果不满足，后面的面值不用看了，因为之前排序过，后面的面值只会越来越大，更加不可能满足条件
                .map(|coin| dp[c - coin as usize].saturating_add(1))
                .min()
                .unwrap_or(std::i32::MAX);
        }

        let res = dp[amount as usize];
        if res != std::i32::MAX {
            res
        } else {
            -1
        }
    }
}

fn main() {
    dbg!(Solution::coin_change(vec![1, 2, 5], 11)); // 3
    dbg!(Solution::coin_change(vec![2], 3)); // -1
    dbg!(Solution::coin_change(vec![1], 0)); // 0
    dbg!(Solution::coin_change(vec![1], 1)); // 1
    dbg!(Solution::coin_change(vec![1], 2)); // 2
    dbg!(Solution::coin_change(
        vec![346, 29, 395, 188, 155, 109],
        9401
    )); // 26
}
