/*
.. default-role:: math

给个字符串，其中最长的回文subsequence（不一定连续）的长度是多少？

最简单的方法是归约到“最长公共subsequence”，复杂度是 `O(n^2)` 。求array和它自身的倒序，即 ``array[:: -1]`` 的最长公共subsequence就可以了。

回忆一下两个array ``s, t`` 的最长公共subsequence怎么求，用DP，定义 `f(i, j)` 为 ``s[..i]`` 和 ``t[..j]`` 的最长公共subsequence的长度。递推式是

.. math::

    f(i, j) = \begin{cases}
        f(i - 1, j - 1) + 1, & \text{ if } s_{i - 1} = t_{j - 1} \\
        \max\{f(i - 1, j), f(i, j - 1)\}, & \text{ otherwise }
    \end{cases}

意思是如果 ``s[i - 1] == t[j - 1]`` ，那么 ``s[i - 1], t[j - 1]`` 可以接在 ``s[..i - 1]`` 和 ``t[..j - 1]`` 的最长公共subsequence后面，使得最长subsequence的长度加1；如果不行，那么最长公共subsequence要么是 ``s[..i - 1]`` 和 ``t[..j]`` 的最长公共subsequence、要么是 ``s[..i]`` 和 ``t[..j - 1]`` 的最长公共subsequence。

最快的方法好像可以做到 `O(n)` ，但是太难理解了，不管了。

注意！最长回文substring（要连续）不能规约到最长公共substring，这是很奇怪的……我也不知道为什么。顺便也回忆一下，也是用DP，定义 ``f(i, j) = T` 为 ``s[i..j]`` 是回文substring。
*/

struct Solution;

use std::cmp::max;

impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut t: Vec<char> = s.clone();
        t.reverse(); // s[:: -1]

        return Solution::longeset_common_subsequence(&s[..], &t[..]) as i32;
    }

    pub fn longeset_common_subsequence<T>(s: &[T], t: &[T]) -> usize
    where
        T: Eq,
    {
        let mut dp = vec![vec![0; t.len() + 1]; s.len() + 1]; // dp[i][j]表示s[0..i]和t[0..j]的最长公共subsequence的长度
        let mut res = 0;

        for i in 1..dp.len() {
            for j in 1..dp[0].len() {
                dp[i][j] = if s[i - 1] == t[j - 1] {
                    // 如果s[i - 1] == t[j - 1]
                    dp[i - 1][j - 1] + 1 // s[i - 1]或t[j - 1]可以接在s[..i - 1]和t[..j - 1]的最长公共subsequence后面
                } else {
                    // 如果不等于
                    max(dp[i - 1][j], dp[i][j - 1]) // 那么s[..i]和t[..j]的最长公共subsequence要么是s[..i - 1]和t[..j]的最长公共subsequence、要么是s[..i]和t[..j - 1]的最长公共subsequence，不会有别的情况
                };
                res = max(res, dp[i][j]);
            }
        }

        res
    }
}

pub fn main() {
    println!(
        "{:?}",
        Solution::longest_palindrome_subseq("bbbab".to_string())
    ); // 4
    println!(
        "{:?}",
        Solution::longest_palindrome_subseq("cbbd".to_string())
    ); // 2
}
