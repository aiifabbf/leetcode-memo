/*
.. default-role:: math

给个array，找到一个数字 `k` ，使得array里面每个数字 `a_i` 除以 `k` 并且向上取整之后的累加和 `\sum_{a_i} \lceil a_i / k \rceil` 小于等于 `t` 。

又是归约……我要二分PTSD了。

这个问题看看上去挺难的，那么不如暂时先不想这个问题了，换个问题：给一个 `k` ，怎样验证array里每个数字除以 `k` 之后的累加和小于等于 `t` 呢？

这也太简单了吧，就这样带进去暴力算一下不就好了嘛，复杂度 `O(n)` 。

所以现在我们有了一个判定函数 ``f: int -> bool`` ， `f(3) = 1` 表示array里面每个数字都除以3再向上取整，加起来累加和小于等于 `t` 。

函数 `f` 有什么性质呢？还真有，它是单调递增的。如果我们能很幸运猜到了一个 `k` 使得 `f(k) = 1` ，那么显然 `f(k + 1) = 1, f(k + 2) = 1` 。

等一下，为啥呢？你想啊，array里每个数字都除以 `k` 之后再加起来，累加和都能小于等于 `t` ，那么每个数字除以更大的 `k + 1` 之后，不是变得更小了吗？那么累加和肯定小于等于之前除以 `k` 的时候。不信给你举个例子

::

    1, 2, 3, 4

原先都除以2再向上取整

::

    1, 1, 2, 2

累加和是6。

现在除以3再向上取整

::

    1, 1, 1, 2

累加和是5。

所以 `f` 写出来肯定是这样的，前面若干个0，之后突然出现了一个1，然后一发不可收拾后面全是1了

::

    1, 2, 3, ..., ?, k, k+1, ...  n
    0, 0, 0, ..., 0, 1, 1, 1, ... f(n)
                   [------------- 成了
    ---------------) 不成

原问题是要我们找到能使得 `f(n) = 1` 的最小的 `n` ，那二分一下不就好了嘛。
*/

struct Solution;

use std::cmp::Ordering;

impl Solution {
    pub fn smallest_divisor(nums: Vec<i32>, threshold: i32) -> i32 {
        let threshold = threshold as u64;

        let feasible = |n| {
            nums.iter()
                .map(|v| (*v as f64 / n as f64).ceil() as u64)
                // .map(|v| (*v as u64 + n - 1) / n) // 好像也没快多少，算了
                .sum::<u64>()
                <= threshold
        };

        // 俗套的二分，找到true第一次出现的位置
        let target = true;
        let mut left = 1;
        let mut right = *nums.iter().max().unwrap_or(&1) as u64;

        while left < right {
            let middle = (left + right) / 2;
            match target.cmp(&feasible(middle)) {
                Ordering::Less => right = middle,
                Ordering::Greater => left = middle + 1,
                Ordering::Equal => right = middle,
            }
        }

        return left as i32;
    }
}

fn main() {
    dbg!(Solution::smallest_divisor(vec![1, 2, 5, 9], 6)); // 5
    dbg!(Solution::smallest_divisor(vec![2, 3, 5, 7, 11], 11)); // 3
    dbg!(Solution::smallest_divisor(vec![19], 5)); // 4
}
