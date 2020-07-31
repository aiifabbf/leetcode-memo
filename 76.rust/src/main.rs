/*
.. default-role:: math

字符串s里面最短的、包含所有t中的字符的substring（要连续）是什么

注意这里的包含是指直方图包含，比如如果t里面有2个 ``a`` ，那么相应地substring里面也至少要有2个 ``a`` 。

又是一个DP结合双指针加速的做法。设 ``dp[j]`` 是以 ``s[j - 1]`` 结尾的最短的满足条件的substring的长度。在算 ``dp[j + 1]`` 的时候，不需要从头开始算，可以直接利用 ``dp[j]`` 。

能用双指针加速的原因是单调性。如果 ``s[i..j]`` 的直方图能完全覆盖t的直方图，那么更大的 ``s[i - 1..j]`` 也一定能覆盖t的直方图；如果 ``s[i..j]`` 的直方图不能完全覆盖t的直方图，那么更小的 ``s[i + 1..j]`` 一定不能。
*/

struct Solution;

use std::collections::BTreeMap;

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        let s: Vec<char> = s.chars().collect();
        let mut counter: BTreeMap<char, usize> = BTreeMap::new(); // 只记录pattern里面有的字符的频次，不记录无关字符
        let mut pattern: BTreeMap<char, usize> = BTreeMap::new(); // t的直方图

        for v in t.chars() {
            *pattern.entry(v).or_insert(0) += 1;
        }

        let mut i = 0;
        let mut res = &[][..];

        for j in 1..s.len() + 1 {
            // 在每次迭代里面，找到以s[j - 1]结尾的最短的substring s[i..j]
            if pattern.contains_key(&s[j - 1]) {
                // 更新一下counter
                *counter.entry(s[j - 1]).or_insert(0) += 1;
            }

            // 如果当前s[i..j]的直方图不足以覆盖t的直方图
            if pattern.iter().any(|(k, v)| {
                if let Some(occurrences) = counter.get(k) {
                    // 某个字符在s[i..j]出现过
                    return occurrences < v; // 但是出现次数不够
                } else {
                    // 根本还没在s[i..j]里出现过
                    return true;
                }
            }) {
                continue; // 那么i不变，j继续增大，希望窗口更大一点之后能使s[i..j]的直方图完全覆盖t的直方图
            }

            // 到这里说明s[i..j]的直方图已经完全覆盖t的直方图了，可以试图缩小s[i..j]、收紧i了

            while i <= j {
                if !pattern.contains_key(&s[i]) {
                    // 如果s[i]根本不是目标字符，都没在t里出现过
                    i += 1; // 那么放心大胆地收紧
                } else {
                    // s[i]在t中出现过
                    if counter.get(&s[i]).unwrap() > pattern.get(&s[i]).unwrap() {
                        // 但是s[i]在s[i..j]中出现的次数大于它在t中出现的次数
                        *counter.get_mut(&s[i]).unwrap() -= 1; // 这时也可以收紧
                        i += 1;
                    } else {
                        // s[i]在s[i..j]中出现的次数等于它在t中出现的次数
                        break; // 不能再收紧了，到此为止了
                    }
                }
            }

            // 到这里就已经算出了对于当前j最短的s[i..j]了

            if res.len() == 0 || j - i < res.len() {
                // 如果比之前记录的还要短
                res = &s[i..j];
            }
        }

        return res.iter().collect();
    }
}

fn main() {
    dbg!(Solution::min_window("ADOBECODEBANC".into(), "ABC".into())); // "BANC"
    dbg!(Solution::min_window("a".into(), "aa".into())); // ""
}
