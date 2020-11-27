/*
.. default-role:: math

给个全是正整数的array，问是否存在一个subsequence（可以不连续）的累加和正好等于整个array的累加和的一半。

比如给 ``[1, 5, 11, 5]`` ，累加和是22，那么 ``[1, 5, 5]`` 和 ``[11]`` 这两个subsequence的累加和是11，正好是22的一半。

想到了两种方法。第一种方法是把所有subsequence可能凑出来的累加和全部放到一个集合里面，然后判断整个array的累加和的一半这个数字在不在集合里面。

递推式也非常好写，假设 `f(j)` 是 ``array[..j]`` 可以凑出的所有累加和，那么

.. math::

    f(j) = f(j - 1) \cup \{v + a_{j - 1} | v \in f(j - 1)\}

很好理解、也很好写，但性能有点差，因为每次都需要建个新的hash set，再和前一个hash set取并集。

还有一种方法是视为0/1背包问题，用动态规划解决，复杂度是 `O(n \sum_{i} a_i)` ，是伪多项式阶的。假设 `f(j, t) = T` 表示 ``array[..j]`` 存在一个subsequence的累加和正好是 `t` 。 `f(j, t)` 为真的条件是啥呢？有两种情况

-   如果 ``array[..j - 1]`` 本身就已经存在一个subsequence的累加和正好是 `t` 了，那么很好办，不取 `a_{j - 1}` 就可以了，直接用 ``array[..j - 1]`` 的subsequence就好了，所以 `f(j, t) = f(j - 1, t)`
-   如果 ``array[..j - 1]`` 本身存在一个累加和正好是 `t - a_{j - 1}` 的subsequence，那么把 `a_{j - 1}` 追加在这个subsequence的后面，就能使得新的subsequence的累加和正好等于 `t` ，所以 `f(j, t) = f(j - 1, t - a_{j - 1})`

这两种情况满足其中任意一种就可以了，所以

.. math::

    f(j, t) = f(j - 1, t) \lor f(j - 1, t - a_{j - 1})

DP的话，就是把 `f(j, t)` 的值全都缓存起来，放在一个二维数组 ``dp`` 里面。
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    // 看array的所有subsequence能凑出哪些累加和
    #[cfg(feature = "set")]
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let summation: i32 = nums.iter().sum();
        if summation % 2 != 0 {
            // 如果整个集合的和是奇数的话，和的一半一定是个xxx.5，因为集合里的数又都是整数，所以子集凑成的和肯定也是整数，无论如何都不可能凑到xxx.5这种数。所以可以直接false掉
            return false;
        }
        let target: i32 = summation / 2;
        let mut summations: HashSet<i32> = HashSet::with_capacity(target as usize + 1); // f(j - 1)

        for v in nums.iter() {
            let mut new_summations: HashSet<i32> = HashSet::with_capacity(target as usize + 1); // 这就是性能差的地方，每次都要重新生成一个新的hash set
            new_summations.insert(*v);

            for w in summations.iter() {
                if (*v + *w) <= target {
                    new_summations.insert(*v + *w);
                }
            }

            // 这时候new_summations等于\{v + a_{j - 1} | v \in f(j - 1)\}

            summations.extend(new_summations.into_iter()); // 然后要和f(j - 1)取并集，又是个很慢的操作
            if summations.contains(&target) {
                return true;
            }
        }

        return false;
    }

    // 看成0/1背包问题，用动态规划
    #[cfg(feature = "dp")]
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let summation = nums.iter().sum::<i32>() as usize;
        if summation % 2 != 0 {
            return false;
        }
        let target = summation / 2;
        let mut dp = vec![vec![false; target + 1]; nums.len() + 1]; // dp[j][t] = f(j, t)，表示array[..j]是否存在一个累加和正好是t的subsequence
        dp[0][0] = true; // 空array的累加和是0

        for i in 1..nums.len() + 1 {
            for t in 0..target + 1 {
                dp[i][t] = if t >= nums[i - 1] as usize {
                    dp[i - 1][t] || dp[i - 1][t - nums[i - 1] as usize]
                } else {
                    dp[i - 1][t]
                }
            }
        }

        return dp[nums.len()][target]; // array[..]存不存在一个subsequence的累加和正好是target呢？
    }
}

pub fn main() {
    println!("{:?}", Solution::can_partition(vec![1, 5, 11, 5])); // true
    println!("{:?}", Solution::can_partition(vec![1, 2, 3, 5])); // false
}
