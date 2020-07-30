/*
.. default-role:: math

给一个字符串中间几个位置插空格，使得每个单词都在字典里出现过，有哪些插法

比如 ``catsanddog`` ，如果给的字典里有这几个词

-   ``cat``
-   ``cats``
-   ``and``
-   ``sand``
-   ``dog``

那么总共有两种拆分方法

-   ``cats and dog``
-   ``cat sand dog``

可以用动态规划。设 ``dp[j]`` 是 ``s[..j]`` 所有的拆分方法，那么 ``dp[j]`` 和前面项的关系是啥呢？假设 ``s[i..j]`` 在字典里面，那么 ``s[i..j]`` 可以单独拆出来形成一个单词，追加到 ``s[..i]`` 的每个拆分方法的后面。

比如 ``catsand`` 里面

-   ``and`` 可以拆出来，那么 ``and`` 可以追加到 ``cats`` 所有的分词方法后面。 ``cats`` 只有一种拆分方法，所以只能形成 ``cats and`` 。
-   ``sand`` 也可以拆出来，那么 ``sand`` 可以追击到 ``cat`` 所有的拆分方法后面。 ``cat`` 同样只有一种拆分方法，所以只能形成 ``cat sand`` 。

所以

.. math::

    \operator{OPT}(j) = \{(x, s[i..j]) | 0 \leq i < j, s[i..j] \in D, x \in \operator{OPT}(i)\}

其中 `(x, s[i..j])` 表示字符串连接。

可想而知如果特地构造字典和句子，会有爆多种组合，这题hard的地方也就在这。有个test case是 ``aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`` （看到里面的那个 ``b`` 了吗）。所以进入正式递推逻辑之前，先判断一下句子里面有没有出现字典里没有出现过的字母，省得算了半天白费功夫。
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        let s: Vec<char> = s.chars().collect();
        let seen: HashSet<Vec<char>> = word_dict
            .into_iter()
            .filter(|v| v.len() <= s.len()) // 去掉比句子本身还长的单词
            .map(|v| v.chars().collect())
            .collect();

        let mut exists = HashSet::new(); // 字典里出现过的所有字符

        for word in seen.iter() {
            for letter in word.iter() {
                exists.insert(letter);
            }
        }

        if s.iter().any(|v| !exists.contains(v)) {
            // 如果句子里面出现了字典里都没出现过的字母
            return vec![]; // 这句子肯定不是用字典里的词语组成的
        }

        let mut dp: Vec<Vec<String>> = vec![vec![]; s.len() + 1]; // dp[j]表示s[..j]的所有拆分方法
        let maximumLength = seen.iter().map(|v| v.len()).max().unwrap_or(0); // 字典里最长的单词的长度

        for j in 1..s.len() + 1 {
            for i in j.checked_sub(maximumLength).unwrap_or(0)..j {
                // 这样就不用每次都从0开始了
                if seen.contains(&s[i..j]) {
                    // s[i..j]在字典里出现过，或者说s[i..j]正好是字典里的某个词语
                    if i == 0 {
                        // i = 0 的情况是初始条件，要特殊处理
                        dp[j].push((&s[i..j]).iter().collect()); // s[..j]这整个句子都是一个单词
                    } else {
                        if !dp[i].is_empty() {
                            let combinations = dp[i] // s[..i]的所有拆分方法
                                .clone()
                                .into_iter()
                                .map(|v| v + " " + &(&s[i..j]).iter().collect::<String>()); // 每种拆分方法后面都追加上s[i..j]这个新的单词
                            dp[j].extend(combinations); // 形成s[..j]的所有拆法
                        }
                    }
                }
            }

            // 这么做就好像失去了用HashSet的意义，如果pattern特别多的话，就显得很低效了
            // for pattern in seen.iter() {
            //     if j >= pattern.len() {
            //         let i = j - pattern.len();
            //         if &s[i..j] == &pattern[..] {
            //             if i != 0 {
            //                 let combinations = dp[i]
            //                     .clone()
            //                     .into_iter()
            //                     .map(|v| v + " " + &(&s[i..j]).iter().collect::<String>());
            //                 dp[j].extend(combinations);
            //             } else {
            //                 dp[j].push((&s[i..j]).iter().collect());
            //             }
            //         }
            //     }

            //     if j >= maximumLength + 1 {
            //         dp[j - maximumLength - 1].clear();
            //     }
            // }
        }

        return dp.last().cloned().unwrap_or(vec![]);

        // return Self::combinations(&s[..], &seen); // 还试过递归写法，也不错，其实是比较自然的写法
    }

    // 递归写法
    // fn combinations(s: &[char], seen: &HashSet<Vec<char>>) -> Vec<String> {
    //     let mut res = vec![];
    //     if seen.contains(s) {
    //         res.push(s.iter().collect());
    //     }

    //     for pattern in seen.iter() {
    //         if s.len() >= pattern.len() {
    //             let j = s.len() - pattern.len();
    //             if &s[j..] == &pattern[..] {
    //                 res.extend(
    //                     Self::combinations(&s[..j], seen)
    //                         .into_iter()
    //                         .map(|v| v + " " + &(&s[j..]).iter().collect::<String>()),
    //                 );
    //             }
    //         }
    //     }

    //     return res;
    // }
}

fn main() {
    dbg!(Solution::word_break(
        "catsanddog".into(),
        vec![
            "cat".into(),
            "cats".into(),
            "and".into(),
            "sand".into(),
            "dog".into(),
        ]
    )); // ["cats and dog", "cat sand dog"]
    dbg!(Solution::word_break(
        "pineapplepenapple".into(),
        vec![
            "apple".into(),
            "pen".into(),
            "applepen".into(),
            "pine".into(),
            "pineapple".into(),
        ]
    )); // ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    dbg!(Solution::word_break(
        "catsandog".into(),
        vec![
            "cat".into(),
            "cats".into(),
            "and".into(),
            "sand".into(),
            "dog".into(),
        ]
    )); // []
    dbg!(Solution::word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".into(),
    vec!["a".into(), "aa".into(), "aaa".into(), "aaaa".into(), "aaaaa".into(), "aaaaaa".into(), "aaaaaaa".into(), "aaaaaaaa".into(), "aaaaaaaaa".into(), "aaaaaaaaaa".into(),]));
    // [] 丧心病狂的test case
}
