/*
.. default-role:: math

给个array，表示每栋房子里的财产数额，不能抢劫相邻的2幢房子，并且房子是环形的，问最多能抢到多少钱。

比如给 ``1, 2, 3, 1`` ，实际上房子的分布是这样的

::

        2
      /   \
    3       1
      \   /
        1

是198题的进阶版。198题里面房子不是成环形的。

那么想想能不能归约到198题。

可以的，我把头尾强行拆开不就好了吗？第一遍不考虑第0栋房子，只考虑 ``array[1..]`` 里的房子；第二遍不考虑最后一栋房子，只考虑 ``array[...-1]`` 里的房子。这样永远不会出现第0栋房子和最后一栋房子同时被抢劫的可能了。

写的数学一点，假设 ``\mathsf{OPT}(0, n)`` 是假设房子不环形排列、考虑 ``array[0..n]`` 的收益，那么如果房子是环形排列的话，最大收益是 ``max(opt(array[1..n]), opt(array[0..n - 1]))``

.. math::

    \max\{\mathsf{OPT}(1, n), \mathsf{OPT}(0, n - 1)\}

*/

struct Solution;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        // 没房子、一幢房子两种情况特殊处理，两栋房子及以上就可以一般处理了
        match nums.len() {
            0 => 0,              // 没房子，啥也抢不到
            1 => 0.max(nums[0]), // 只有一栋房子，要不要抢呢，有没有可能有负财产呢
            _ => Self::opt(&nums[1..]).max(Self::opt(&nums[..nums.len() - 1])),
        }
    }

    // 把198抄了一遍……
    fn opt(array: &[i32]) -> i32 {
        match array.len() {
            0 => 0,
            1 => 0.max(array[0]),
            _ => {
                let mut dp = vec![0; array.len() + 1]; // dp[i]表示只考虑array[..i]里的房子，最多能抢到多少钱
                dp[0] = 0; // array[..0]里没房子，所以没钱
                dp[1] = 0.max(array[0]); // array[..1]里只有一栋房子

                for i in 2..array.len() + 1 {
                    dp[i] = (array[i - 1] + dp[i - 2]).max(dp[i - 1]); // 如果抢第i - 1间房子，那么第i - 2就肯定不能抢，所以最大收益是第i - 1间房子的财产加上考虑array[0..i - 2]里的最大收益；如果不抢第i - 1间房子，那么最大收益是考虑array[0..i - 1]里的最大收益
                }

                dp.into_iter().max().unwrap_or(0)
            }
        }
    }
}

fn main() {
    dbg!(Solution::rob(vec![2, 3, 2])); // 3
    dbg!(Solution::rob(vec![1, 2, 3, 1])); // 4
    dbg!(Solution::rob(vec![0])); // 0
    dbg!(Solution::rob(vec![])); // 0
    dbg!(Solution::rob(vec![1])); // 1
}
