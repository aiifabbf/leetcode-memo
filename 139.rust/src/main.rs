/*
.. default-role:: math

给一个句子和一个字典，问能否只用字典里的词语连接组成这个句子。每个词语都可以用无限多次。

比如给个句子 ``applepenapple`` ，字典是 ``apple, pen`` 这2个词语， ``applepenapple`` 确实可以用这两个词语组成，比如 ``apple pen apple`` 。

用动态规划可以解决。设 ``dp[j] == true`` 表示 ``s[..j]`` 可以用字典里的单词连接组合而成。那么 ``dp[j] == true`` 成立的条件是什么呢？如果我们能找到一个 `i` ，使得 ``s[..i]`` 可以用字典的词语组成，并且 ``s[i..j]`` 也恰好是字典里的某个词语，那么 ``s[..j]`` 整个不就可以全部用字典里的词语连接组成了吗？

比如你看 ``applepen`` 可以用 ``apple, pen`` 组成，同时 ``apple`` 也正好是字典里的一个词语，所以 ``applepenapple`` 整个都可以完全用字典里的词语组成。

140的简化版。140要求出具体的组合方式，而这一题只要判断能否组成。

有两个加速小技巧

-   进入正式逻辑之前，可以先把字典里出现过的所有字符都记下来，再去看字符串里有没有出现过字典里没有出现过的字符，如果出现了，那么字符串必不可能用字典里的词组成。
-   记录一下字典里出现过的最长的单词的长度，假设是 `m` ，那么搜索 `i` 的时候，可以直接从 `j - m` 开始搜索，而不需要每次都从0开始搜索。
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let s: Vec<char> = s.chars().collect();
        let seen: HashSet<Vec<char>> = word_dict
            .into_iter()
            .filter(|v| v.len() <= s.len()) // 过滤掉长度大于句子本身的词语
            .map(|v| v.chars().collect())
            .collect();
        let maximumLength = seen
            .iter()
            .map(|v| v.len())
            .max()
            .unwrap_or(std::usize::MAX); // 小技巧1，字典里出现的最长的单词的长度
        let mut dp = vec![false; s.len() + 1]; // dp[j] == true表示s[..j]可以用字典里的词语连接组合而成
        dp[0] = true;

        for j in 1..s.len() + 1 {
            if (j.checked_sub(maximumLength).unwrap_or(0)..j)
                .any(|i| dp[i] == true && seen.contains(&s[i..j]))
            {
                // 如果存在一个i属于[j - m, j)，并且dp[i] = true、s[i..j]也正好是字典里的词语的话
                dp[j] = true; // 那么s[..j]可以拆成s[..i]和s[i..j]两部分，第一部分s[..i]可以用字典里的词构成，第二部分s[i..j]正好就是字典里的某个词，那么s[..j]整个都可以用字典里的词构成
            }
        }

        return dp.last().cloned().unwrap_or(false);
    }
}

fn main() {
    dbg!(Solution::word_break(
        "leetcode".into(),
        vec!["leet".into(), "code".into(),]
    )); // true
    dbg!(Solution::word_break(
        "applepenapple".into(),
        vec!["apple".into(), "pen".into(),]
    )); // true
    dbg!(Solution::word_break(
        "catsandog".into(),
        vec![
            "cats".into(),
            "dog".into(),
            "sand".into(),
            "and".into(),
            "cat".into(),
        ]
    )); // false
}
