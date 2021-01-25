/*
.. default-role:: math

给个24小时制的pattern，类似 ``2?:?0`` ， ``?`` 能匹配任何数字，但是要保证小时和分钟的范围正确，比如不能出现 ``25`` 小时、 ``70`` 分钟。问匹配成功的最大时间是多少？

比如和 ``2?:?0`` 能匹配成功的最大时间是 ``23:50`` 。

Python用的是快很多、但是写起来很啰嗦的方法，针对不同的pattern分情况处理。

这里用Rust写的方法是暴力从23:59往下到00:00，一个一个测试是否匹配，如果匹配成功，那么这个时间就是答案了。

好处就在于写的舒服……（也并不是很暴力，总共也只需要测试24 * 60种情况）
*/

struct Solution;

impl Solution {
    pub fn maximum_time(time: String) -> String {
        (0..60 * 24)
            .rev() // 从23:59往下到00:00
            .map(|timestamp| {
                let hour = format!("{:0>2}", timestamp / 60); // 右对齐，前面补零，直到成为两位数
                let minute = format!("{:0>2}", timestamp % 60);
                format!("{}:{}", hour, minute)
            })
            .filter(|combined| {
                time.chars()
                    .zip(combined.chars())
                    .all(|(p, s)| p == '?' || p == s) // 如果是问号，能匹配任何数字；如果是数字，只能匹配那个数字
            }) // 试试ab:cd和2?:?0是否匹配
            .next() // 第一个匹配成功的就是答案
            .unwrap_or("00:00".to_owned())
    }
}

fn main() {
    dbg!(Solution::maximum_time("2?:?0".to_owned())); // 23:50
    dbg!(Solution::maximum_time("0?:3?".to_owned())); // 09:39
}
