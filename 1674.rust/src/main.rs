/*
.. default-role:: math

给一个包含偶数个元素的的array和一个数字 `l` ，每次修改可以把array里任意一个数字替换成 `[1, l]` 里的任意整数。问最少需要多少次修改才能使得array满足“互补”的性质。所谓互补就是对于任意 `i, j` 都有 `a_i + a_{n - i - 1} = a_j + a_{n - j - 1}` 。

这样写出来可能不太直观，举个例子，比如 ``[1, 2, 3, 4]`` 就是互补的，因为

::

    1, 2, 3, 4
       |--|
    |--------|

`1 + 4 = 5` ，同样 `2 + 3 = 5` 。

或者说，如果你把array想象成一个纸带，从最中间剪开

::

    1, 2 | 3, 4

把右半部分向左折叠过来

::

    4, 3 |
    1, 2 |

然后竖着每一列加起来

::

    4, 3 |
    1, 2 |
    5, 5 =

有点难，要绕好几个弯。

题目要求要最少回合，那么我们看一下，对于 `a_i, a_{n - i - 1}` 这一对数字，花费0次机会、花费1次机会、花费2次机会分别能达成什么效果。为什么不考虑花费3回合？因为3回合没有意义，一对数字总共就2个数字。

-   花费0次机会，也就是完全不动， `a_i + a_{n - i - 1}` 保持不变
-   花费1次机会，只修改1个数字， `a_i + a_{n - i - 1}` 最小可以到 `\min\{a_i + a_{n - i - 1}\} + 1` ，最大可以到 `\max\{a_i + a_{n - i - 1}\} + l`
-   花费2次机会，修改2个数字，可以让 `a_i + a_{n - i - 1}` 变成 `[2, 2l]` 里的任意一个数字

反过来说，要把和修改到某个数字需要多少次修改机会呢？设 `m, M` 分别是 `a_i, a_{n - i - 1}` 里较小的那个数、较大的那个数，即 `m = \min\{a_i + a_{n - i - 1}\}, M = \max\{a_i + a_{n - i - 1}\}`

-   要把和修改到 `[2, m + 1)` 中的某个数需要2次机会
-   要把和修改到 `[m + 1, m + M)` 中的某个数需要1次机会
-   要把和修改到 `[m + M, m + M + 1)` 中的某个数需要0次机会
-   要把和修改到 `[m + M + 1, M + l + 1)` 中的某个数需要1次机会
-   要把和修改到 `[M + l + 1, 2l + 1)` 中的某个数需要2次机会

看起来像是个直方图，画个图出来

::

        2                                2
    |--------|                       |--------|
    |        |    1             1    |        |
    |        |--------|     |--------|        |
    |        |        |  0  |        |        |
    |--------|--------|-----|--------|--------|
    2       m+1      m+M   m+M+1   M+l+1     2l+1

这个直方图的差分是

::

    +2
    |                       +1       +1
    |                       |        |
    |--------|--------|-----|--------|--------|
             |        |                       |
             -1       -1                      |
                                              -2

当然这只是一对数字的情况，其他数字怎么办呢？把每个数字对应的直方图都加起来，直方图里最小的频次就是答案了。

因为微积分是线性的，所以可以把 `n / 2` 对数字的直方图的差分累加起来，一起整个积分，结果和直方图本身累加起来完全相等。

.. 我觉得这篇写的很差，不知道该怎么讲清楚，不知道你有没有看懂……
*/

struct Solution;

impl Solution {
    pub fn min_moves(nums: Vec<i32>, limit: i32) -> i32 {
        let limit = limit as usize; // 每回合只能把任意数字变成[1, l]中的某个整数
        let length = nums.len();
        let mut derivatives = vec![0; 2 * limit + 2]; // 导函数

        for (v, w) in nums
            .iter()
            .cloned()
            .take(length / 2) // 取前n / 2个数字
            .zip(nums.iter().skip(length / 2).rev().cloned())
        // 和后n / 2个数字、并且折叠后的zip起来，这样第i轮遍历的就是(a[i], a[n - i - 1])了
        {
            // v = a[i], w = a[n - i - 1]
            let (min, max) = (v.min(w) as usize, v.max(w) as usize); // 给v、w排序，假设min是v、w里较小的那个数，max是v、w里较大的那个数

            // 修改2次，可以让a[i] + a[n - i - 1]变成[2, 2l + 1)里任意一个整数
            derivatives[2] += 2; // 对应图上2处的+2
            derivatives[2 * limit + 1] -= 2; // 对应图上2l+1处的-2
            // 修改1次，可以让a[i] + a[n - i - 1]变成[min + 1, max + l + 1)里任意一个整数
            derivatives[min + 1] -= 1;
            derivatives[max + limit + 1] += 1;
            // 修改0次，a[i] + a[n - i - 1]只能是原来的值，也就是变成[min + max, min + max + 1)里任意一个整数
            derivatives[min + max] -= 1;
            derivatives[min + max + 1] += 1;
        }

        let counter: Vec<i32> = derivatives
            .iter()
            .scan(0, |state, v| {
                *state = *state + *v;
                Some(*state)
            })
            .collect(); // 给导函数积分，恢复出原函数。counter[k] = v表示，令任意a[i] + a[n - i - 1] = k最少需要修改v次

        counter
            .into_iter()
            .take(2 * limit + 1) // counter的key的范围是[2, 2l]
            .skip(2) // 和不可能是0、1，忽略
            .min()
            .unwrap_or(0)
    }
}

fn main() {
    dbg!(Solution::min_moves(vec![1, 2, 4, 3], 4)); // 1
    dbg!(Solution::min_moves(vec![1, 2, 2, 1], 2)); // 2
    dbg!(Solution::min_moves(vec![1, 2, 1, 2], 2)); // 0
}