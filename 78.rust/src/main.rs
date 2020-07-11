/*
.. default-role:: math

给一个集合，找到这个集合所有的子集

含有 `n` 个元素的集合总共有 `2^n` 个子集。

可以用动态规划的思路做，先把集合看成是array，设 ``dp[i]`` 是前 `i` 个元素可以构成的所有子集。比如 ``{1, 2, 3, 4}`` ， ``dp[2]`` 就是

::

    {
        {},
        {1},
        {2},
        {1, 2},
    }

``dp[3]`` 就是

::

    {
        {},
        {1},
        {2},
        {1, 2},
        {3},
        {1, 3},
        {2, 3},
        {1, 2, 3},
    }

观察一下，能发现 ``dp[i]`` 由两部分构成

-   ``dp[i - 1]`` 里的每个集合
-   ``dp[i - 1]`` 里每个集合加上 ``a[i - 1]``

比如 ``dp[3]`` 就是

::

    {
        {}, // 来自dp[2]
        {1}, // 来自dp[2]
        {2}, // 来自dp[2]
        {1, 2}, // 来自dp[2]
        {3}, // {} + 3
        {1, 3}, // {1} + 3
        {2, 3}, // {2} + 3
        {1, 2, 3}, // {1, 2} + 3
    }

因为 ``dp[i]`` 只和 ``dp[i - 1]`` 有关，所以可以只存 ``dp[i - 1]`` 。最后结果就是 ``dp[-1]`` 。
*/

struct Solution;

use std::collections::BTreeSet;
use std::collections::HashSet;

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        // HashSet没法存HashSet，因为HashSet没有实现Hash，但是BTreeSet实现了Hash
        let mut res: HashSet<BTreeSet<i32>> = HashSet::new(); // dp[i - 1]
        res.insert(BTreeSet::new()); // 空集也是其中一个子集，不要忘记了

        for v in nums.into_iter() {
            let mut subset = HashSet::new(); // 前i个元素能构成的所有子集

            for w in res.iter() {
                // 遍历dp[i - 1]里的每个集合
                let mut set = w.clone();
                set.insert(v); // 每个集合都加上a[i - 1]
                subset.insert(set);
            }

            res.extend(subset.into_iter());
        }

        return res.into_iter().map(|v| v.into_iter().collect()).collect();
    }
}

fn main() {
    println!("{:#?}", Solution::subsets(vec![1, 2, 3]));
}
