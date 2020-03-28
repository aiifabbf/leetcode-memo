/*
.. default-role:: math

给一个全是0和1的array，最长的全1 substring（要连续）的长度是多少

DP最好做。设 ``dp[i]`` 是以第 `i - 1` 个元素结尾的最长的全1 substring的长度。递推式很容易写出来

.. math::

    \operatorname{OPT}(i) = \begin{cases}
        \operatorname{OPT}(i - 1) + 1, & a_{i - 1} = 1 \\
        0, & a_{i - 1} = 0 \\
    \end{cases}

也就是

-   如果第 `i - 1` 个元素正好是1，那么可以接在以前一个元素结尾的最长全1 substring的后面，所以以第 `i - 1` 个元素结尾的最长substring就是以第 `i - 2` 个元素结尾的最长substring的长度加1
-   如果第 `i - 1` 个元素是0，那很抱歉，前面再长也没用，以第 `i - 1` 个元素结尾的最长substring的长度只能是0

初始条件是 `\operatorname{OPT}(0) = 0` ，因为空array的最长全1 substring的长度是0。

原问题的解就是最大的 ``dp[i]`` ，也就是 `\max\{\operatorname{OPT}(i)\}` 。

还可以优化一下空间复杂度。递推式只和前一项有关，所以可以只保留前一项。
*/

struct Solution;

use std::cmp::max;

impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut lastDp = 0; // 递推式只和前一项有关，所以只保留前一项

        for v in nums.into_iter() {
            if v == 1 {
                lastDp = lastDp + 1;
            } else {
                lastDp = 0;
            }

            res = max(res, lastDp); // 一边遍历一边更新目前见过的最大值
        }

        return res;
    }
}

pub fn main() {
    println!(
        "{}",
        Solution::find_max_consecutive_ones(vec![1, 1, 0, 1, 1, 1])
    ); // 3
    println!(
        "{}",
        Solution::find_max_consecutive_ones(vec![1, 1, 0, 1, 1, 1, 0, 1])
    ); // 3
    println!("{}", Solution::find_max_consecutive_ones(vec![0, 0, 0])); // 0
    println!("{}", Solution::find_max_consecutive_ones(vec![])); // 0
}
