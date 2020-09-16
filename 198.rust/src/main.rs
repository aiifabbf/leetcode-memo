/*
.. default-role:: math

第 `i` 家有 ``nums[i]`` 财产，不能抢连续两家，问最多能抢到多少钱？

比如给 ``2, 1, 1, 2`` ，有这几种方案

::

    2 1 1 2
            0，一家都不抢
    ^       2
      ^     1
        ^   1
          ^ 2
    ^   ^   3
    ^     ^ 4
      ^   ^ 3
        ^   1
          ^ 2

可见最大收益是4。

设 ``dp[i]`` 只抢前 `i` 家赚到的最大收益。那么 ``dp[i]`` 怎么用前面的项算出来呢？对于第 `i - 1` 家，只有抢和不抢两种选择

-   如果不抢，那么最大收益一定是 ``dp[i - 1]``
-   如果抢，那么第 `i - 2` 家必定不能抢，最大收益是抢前 `i - 2` 家的最大加上抢第 `i - 1` 家的收益

::
               i-1
    ... | 2 | 3 | 4 |
           i-2      i
    ------------|      不抢第i - 1家
    --------|   |---|  抢第i - 1家
*/

struct Solution;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() <= 2 {
            return nums.into_iter().max().unwrap_or(0);
        }

        let mut dp = vec![0; nums.len() + 1];
        // 初始条件
        dp[0] = 0;
        dp[1] = 0.max(nums[0]);
        dp[2] = 0.max(nums[0]).max(nums[1]);

        for i in 3..nums.len() + 1 {
            dp[i] = dp[i - 1] // 不抢第i - 1家，收益是抢前i - 1家的最大收益
                .max(nums[i - 1] + dp[i - 2]); // 抢第i - 1家，收益第i - 1家的收益加上前i - 1家的最大收益
        }

        return *dp.last().unwrap();
    }
}

fn main() {
    dbg!(Solution::rob(vec![1, 2, 3, 1])); // 4
    dbg!(Solution::rob(vec![2, 7, 9, 3, 1])); // 12
    dbg!(Solution::rob(vec![2, 1, 1, 2])); // 4
}
