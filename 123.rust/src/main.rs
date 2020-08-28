/*
.. default-role:: math

最多只能交易两次，且手上最多只能持有一种股票，问最大收益。

可以归约到之前的只能最多交易一次的问题。首先选择一个切点 `i` ，把array分成两部分 ``array[..i]`` 和 ``array[i..]`` ，每部分内部只能最多交易一次，即 ``array[..i]`` 里只能最多交易一次、 ``array[i..]`` 最多只能交易一次。假设 ``f(array[..i])`` 是前 `i` 天的最大收益，那么整个array的收益就是

-   ``f(array[..0]) + f(array[0..])``
-   ``f(array[..1]) + f(array[1..])``
-   ``f(array[..2]) + f(array[2..])``
-   ...
-   ``f(array[..n - 1]) + f(array[n - 1..])``
-   ``f(array[..n]) + f(array[n..])``

中最大的那个。

在最多交易一次的那个问题里，算出一个array的最大收益是 `O(n)` ，所以如果我们这边不加什么优化，那么算出每个切点 `i` 的收益的复杂度就是 `O(n)` ，算出所有切点的收益的最大值就是 `O(n^2)` 了。

那来思考一下这种方法有没有重复计算。其实是有的，算 ``f(array[..5])`` 的时候，能不能利用一下 ``f(array[..4])`` 已经算出来的结果、而不是重新从头算起？

是可以的，因为对于第 `i - 1` 天只有两种选择

-   不卖出，那么收益和前一天一样，也就是 ``f(array[..i - 1])``
-   卖出，那么最大收益是第 `i - 1` 天的价格减去前 `i - 1` 天见过的最低价，也就是 ``array[i - 1] - min(array[..i - 1])``

即

::

    f(array[..i]) = max(
        f(array[..i - 1]),
        array[i - 1] - min(array[..i - 1])
    )

对于 ``f(array[i..])`` 也是同理，只不过颠倒过来，对于第 `i` 天而言只有两种选择

-   不卖出，那么收益和后一天相同，也就是 ``f(array[i + 1..])``
-   卖出，那么最大收益是第 `i + 1` 天及之后见过的最高价减去第 `i ` 天的价格，也就是 ``max(array[i + 1..]) - array[i]``

即

::

    f(array[i..]) = max(
        f(array[i + 1..]),
        max(array[i + 1..]) - array[i]
    )
*/

struct Solution;

impl Solution {
    // O(n^2)做法，每遇到一个新的i，都要重新算一遍prices[..i]和prices[i..]的收益之和
    // pub fn max_profit(prices: Vec<i32>) -> i32 {
    //     let mut res = 0;

    //     for i in 0..prices.len() + 1 {
    //         res = res.max(
    //             Self::max_profit_max_one_transaction(&prices[..i])
    //                 + Self::max_profit_max_one_transaction(&prices[i..]),
    //         );
    //     }

    //     return res;
    // }

    // fn max_profit_max_one_transaction(prices: &[i32]) -> i32 {
    //     let mut res = 0;
    //     let mut minimum = std::i32::MAX;

    //     for v in prices.iter() {
    //         res = res.max(v.checked_sub(minimum).unwrap_or(0));
    //         minimum = minimum.min(*v);
    //     }

    //     return res;
    // }

    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.len() < 2 {
            return 0;
        }

        let mut before = vec![0; prices.len() + 1]; // before[i]表示prices[..i]最多只能交易一次能达成的最大收益，或者说是前i天最多只能交易一次能达成的最大收益
        let mut after = vec![0; prices.len() + 1]; // after[i]表示prices[i..]最多只能交易一次能达成的最大收益，或者说是后i天最多只能交易一次能达成的最大收益

        // 先算出before
        let mut minimum = prices[0]; // 记下前面见过的最小值

        for i in 2..prices.len() + 1 {
            before[i] = before[i - 1].max(prices[i - 1] - minimum); // 前i天的最大收益等于前i - 1天的最大收益、或者第i - 1天卖出的最大收益
            minimum = minimum.min(prices[i - 1]); // 更新见过的最小值
        }

        // 再算出after
        let mut maximum = prices[prices.len() - 1]; // 后面见过的最大值

        for i in (0..prices.len() - 1).rev() {
            after[i] = after[i + 1].max(maximum - prices[i]); // 第i天开始的最大收益是第i + 1天开始的最大收益、或者第i + 1天之后见过的最高价减去第i天的价格
            maximum = maximum.max(prices[i]);
        }

        let mut res = 0;

        for i in 0..prices.len() + 1 {
            res = res.max(before[i] + after[i]); // array[..i]里最多只能交易一次、array[i..]里最多只能交易一次
        }

        return res;
    }
}

fn main() {
    dbg!(Solution::max_profit(vec![3, 3, 5, 0, 0, 3, 1, 4])); // 6
    dbg!(Solution::max_profit(vec![1, 2, 3, 4, 5])); // 4
    dbg!(Solution::max_profit(vec![7, 6, 4, 3, 1])); // 0
}
