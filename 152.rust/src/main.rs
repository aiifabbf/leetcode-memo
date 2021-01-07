/*
.. default-role:: math

给个array，乘积最大的非空substring（要连续）的乘积是多少？

比如给 ``2, 3, -2, 4`` ，所有的substring是

::

    [2] -> 2
    [3] -> 2
    [-2] -> -2
    [4] -> 4
    [2, 3] -> 6
    [3, -2] -> -6
    [-2, 4] -> -8
    [2, 3, -2] -> -12
    [3, -2, 4] -> -24
    [2, 3, -2, 4] -> -48

最大乘积是 ``[2, 3]`` 这个substring凑出来的6。

看到substring就是传统艺能动态规划，一般没错，即使有错都能强行凑成动态规划。设 ``dp[i]`` 是以第 `i` 个元素结尾的substring的最大积。想一想和前面的项有什么关系

-   如果 ``array[i]`` 是0，那么很简单， ``dp[i]`` 直接是0，因为以第 `i` 个元素结尾的非空substring一定要带一个 ``array[i]`` ，而 ``array[i]`` 又是0，前面的积再大都没有，遇到这个0一乘还是变成0
-   如果 ``array[i]`` 不是0，那么有点复杂，有三种情况

    -   可能 ``[array[i]]`` 这个只含一个元素的substring就已经是以 ``array[i]`` 结尾的乘积最大的substring
    -   也有可能 ``array[i]`` 接在以 ``array[i - 1]`` 结尾的乘积最大的substring后面，能组成一个更大的乘积
    -   还有一种很容易漏掉的情况，有可能 ``array[i]`` 接在以 ``array[i - 1]`` 结尾的、 **乘积最小** 的substring后面，反而能组成更大的乘积

        这种情况看上去很反直觉，其实有道理的，因为没有说array里面不能有负数。假如 ``array[i]`` 是个负数，而以 ``array[i - 1]`` 结尾的substring的最大乘积是个正数、最小乘积是个负数，那么可想而知， ``array[i]`` 接在最小乘积后面反而能凑成一个正数乘积，反而更大。

假设 `f(i)` 是以 ``array[i]`` 结尾的最大乘积， `g(i)` 是以 ``array[i]`` 结尾的最小乘积，递推式是

.. math::

    \begin{aligned}
        f(i) &= \max\{ a_i, a_i f(i - 1), a_i g(i - 1) \} \\
        g(i) &= \min\{ a_i, a_i g(i - 1), a_i f(i - 1) \} \\
    \end{aligned}

初始条件是

.. math::

    \begin{aligned}
        f(0) &= a_0 \\
        g(0) &= a_0 \\
    \end{aligned}
*/

struct Solution;

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            // 其实这个未定义
            return 0;
        }

        let mut maximums = vec![0; nums.len()]; // maximums[i]是以第i个元素结尾的、积最大的substring的积
        let mut minimums = vec![0; nums.len()]; // minimums[i]是以第i个元素结尾的、积最小的substring的积

        // 初始条件
        maximums[0] = nums[0]; // 以第0个元素结尾的最大积只能是本身，因为substring不能为空，必须得选一个
        minimums[0] = nums[0]; // 以第0个元素结尾的最小积只能是本身

        // 然后开始递推
        for (i, v) in nums.iter().cloned().enumerate().skip(1) {
            if v == 0 {
                // 如果是0
                maximums[i] = 0; // 那么以第i个元素结尾的substring一定要带上这个0，所以积被强行拉成0
                minimums[i] = 0; // 同理
            } else {
                // 如果不是0
                maximums[i] = v.max(maximums[i - 1] * v).max(minimums[i - 1] * v); // f(i)
                minimums[i] = v.min(minimums[i - 1] * v).min(maximums[i - 1] * v);
                // g(i)
            }
        }

        return maximums.into_iter().max().unwrap_or(0);
    }
}

fn main() {
    dbg!(Solution::max_product(vec![2, 3, -2, 4])); // 6
    dbg!(Solution::max_product(vec![-2, 0, -1])); // 0
}
