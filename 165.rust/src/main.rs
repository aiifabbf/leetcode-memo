/*
.. default-role:: math

比较两个版本号谁高谁低。

版本号有点像字典序，比如 `0.1 < 1.1, 1.0.1 > 1, 7.5.2.4 < 7.5.3` ，又和字典序有点差别，比如在有0的时候，比如 `1.0.0 = 1.0 = 1, 1.001 = 1.01` 。

把字典序的比较过程稍微魔改一下就好了。
*/

struct Solution;

impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let mut numbers1 = version1.split(".").map(|v| v.parse::<i32>().unwrap()); // parse把字符串001和1都变成数字1
        let mut numbers2 = version2.split(".").map(|v| v.parse::<i32>().unwrap());

        loop {
            match (numbers1.next(), numbers2.next()) {
                (Some(v), Some(w)) => {
                    if v > w {
                        return 1;
                    } else if v < w {
                        return -1;
                    } // 如果相等，继续看下一位
                }
                (Some(v), None) => {
                    // 这是和字典序不一样的地方。如果是字典序，这里肯定是number2更大。但在这里要当做是0，因为可能有1.0.0 == 1.0的情况
                    if v > 0 {
                        return 1;
                    } else if v < 0 {
                        return -1;
                    } // 如果相等，继续看下一位
                }
                (None, Some(w)) => {
                    // 同理
                    if 0 > w {
                        return 1;
                    } else if 0 < w {
                        return -1;
                    }
                }
                (None, None) => {
                    // 前面的所有位都比完了，还是没比出大小，说明真的一样大
                    return 0;
                }
            }
        }
    }
}

fn main() {
    dbg!(Solution::compare_version("0.1".into(), "1.1".into())); // -1
    dbg!(Solution::compare_version("1.0.1".into(), "1".into())); // 1
    dbg!(Solution::compare_version("7.5.2.4".into(), "7.5.3".into())); // -1
    dbg!(Solution::compare_version("1.01".into(), "1.001".into())); // 0
}
