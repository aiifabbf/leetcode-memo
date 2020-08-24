/*
.. default-role:: math

给个字符串，第 `i` 步只能选其中一个字符，给它的ascii码加 `i` 。一个字符只能加一次。注意这个加是循环的，如果给 ``z`` 加上1，那么 ``z`` 会变成 ``a`` 。问能否在 `k` 步内完成。

比如 ``aab`` 变成 ``bbb`` 。首先第1步可以把第一个 ``a`` 位移1个单位变成 ``b`` ，但是要到第27步才能把第二个 ``a`` 位移27个单位变成 ``b`` 。所以最少需要27步。

难点就在于要记住之前用过了哪几步。所以用一个hash map来存所有已经用过的位移。比如 ``seen[2] == [2, 28, 54]`` 表示已经出现过3个需要位移2次的字符了，但是因为冲突的问题，除了第一个字符可以在第2步的时候通过位移2个单位实现，第二个字符必须要通过在第28步的时候位移28个单位才能实现位移2个单位的效果，第三个字符必须要通过在第54步位移54个单位才能实现同样的位移2个单位的效果。此后如果再遇到一个字符需要位移2次，很容易就能知道这一次必须要在第 `54 + 26 = 80` 步、位移80个单位才能移动到本来位移2次就能到达的位置。
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn can_convert_string(s: String, t: String, k: i32) -> bool {
        if s.len() != t.len() {
            // 如果长度都不相等
            return false; // 那绝对没可能
        }

        let mut minimum = 0; // 最少需要多少步
        let mut seen: HashMap<usize, Vec<usize>> = HashMap::new(); // 见过的位移，和+ 26 * k的版本，比如假设seen[2] = [2, 28, 54]说明字符串里出现了多个位置需要位移2个单位，但是因为每一步只能移动一个字符，所以同样要位移2个单位，第一个字符（假设是a -> c）可以直接在第2步位移2个单位，而第二个字符（假设是b -> d）必须要等到第28步、位移28个单位才能达到和移动2次相同的效果

        for (v, mut w) in s
            .chars()
            .map(|v| v as usize - 'a' as usize)
            .zip(t.chars().map(|v| v as usize - 'a' as usize))
        {
            if w == v {
                // 如果两个字符相同
                continue; // 不需要位移
            }

            if w < v {
                // 如果目标字符反而比源字符还小，比如b -> a
                w = w + 26; // 那么肯定是要先转一个周期
            }

            let delta = w - v; // 最小位移
            let mut step = delta; // 实际位移

            match seen.get_mut(&delta) {
                Some(steps) => {
                    // 之前已经有个字符在第2步位移了2个单位、有个字符在第28步位移了28个单位
                    step = steps.last().unwrap() + 26; // 这次只能在第28 + 26 = 54步位移54个单位了
                    steps.push(step);
                }
                None => {
                    // 之前没有字符在第2步位移2个单位
                    seen.insert(delta, vec![step]);
                }
            }

            minimum = minimum.max(step); // 更新全局最小步数
            if minimum > k as usize {
                // 如果这时候已经大于k了
                return false; // 必不可能
            }
        }

        return minimum <= k as usize;
    }
}

fn main() {
    dbg!(Solution::can_convert_string(
        "input".into(),
        "ouput".into(),
        9
    )); // true
    dbg!(Solution::can_convert_string("abc".into(), "bcd".into(), 10)); // false
    dbg!(Solution::can_convert_string("aab".into(), "bbb".into(), 27)); // true
    dbg!(Solution::can_convert_string(
        "iqssxdlb".into(),
        "dyuqrwyr".into(),
        40
    )); // true
}
