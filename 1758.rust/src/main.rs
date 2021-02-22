/*
.. default-role:: math

给一个只包含 ``0, 1`` 的字符串，问最少需要toggle几次，才能让字符串变成类似 ``010101...`` 或者 ``101010...`` 这样的交替字符串。

比如给个 ``0100`` ，只要把最后的0变成1，整个字符串会变成满足条件的 ``0101`` 。所以只要toggle一次。

很简单，因为只会有两种字符串，所以两种都试一下，看哪个需要的toggle次数最少。
*/

struct Solution;

impl Solution {
    pub fn min_operations(s: String) -> i32 {
        s.chars()
            .zip(['0', '1'].iter().cloned().cycle()) // ['0', '1'].iter().cloned().cycle()用来生成0, 1, 0, 1, ...的无限序列
            .filter(|(v, w)| v != w) // 过滤出所有需要toggle的位置
            .count() // 统计
            .min(
                s.chars()
                    .zip(['1', '0'].iter().cloned().cycle())
                    .filter(|(v, w)| v != w)
                    .count(),
            ) as i32 // 函数式太爽了
    }
}

fn main() {
    dbg!(Solution::min_operations("0100".to_owned())); // 1
    dbg!(Solution::min_operations("10".to_owned())); // 0
    dbg!(Solution::min_operations("1111".to_owned())); // 2
}
