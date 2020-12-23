/*
.. default-role:: math

把电话号码格式化成为每3个数字为一段，如果最后一段剩下了4个数字，分成2+2。

比如 ``123456`` 变成 ``123-456`` ， ``1234567`` 变成 ``123-45-67`` ， ``12345678`` 变成 ``123-456-78`` 。
*/

struct Solution;

impl Solution {
    pub fn reformat_number(number: String) -> String {
        let mut res: Vec<String> = vec![];
        let mut buffer = vec![]; // 暂存，达到3个数字之后放入res

        for v in number.chars() {
            if v.is_ascii_digit() {
                if buffer.len() == 3 {
                    res.push(buffer.into_iter().collect());
                    buffer = vec![v];
                } else {
                    buffer.push(v);
                }
            }
        }

        if res.len() >= 1 && buffer.len() == 1 {
            // 如果最后一段剩下1个数字、上一段正好是3个数字，那么说明最后剩下了4个数字，要分成2 + 2
            let mut last = res.pop().unwrap(); // 上一段是456
            last.extend(buffer.into_iter()); // buffer里面是7
            let a = last[0..2].to_owned();
            let b = last[2..].to_owned();
            res.push(a);
            res.push(b);
        } else {
            // 其他情况无脑把buffer放到res里
            res.push(buffer.into_iter().collect());
        }

        res.join("-")
    }
}

fn main() {
    dbg!(Solution::reformat_number("1-23-45 6".to_owned())); // 123-456
    dbg!(Solution::reformat_number("123 4-567".to_owned())); // 123-45-67
    dbg!(Solution::reformat_number("123 4-5678".to_owned())); // 123-456-78
}
