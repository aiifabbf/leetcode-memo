/* 
.. default-role:: math

计算两个超长的二进制数

没啥难的，按部就班地写就好了。但是要写的好看也挺难的，因为两个二进制数的位数不一定相等，所以指针从低位移动到高位的时候，总是会出现有一个数已经遍历完的情况。此时高位应该补0。
*/

struct Solution;

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let a: Vec<u8> = a
            .chars()
            .rev() // chars()居然返回的是一个可逆迭代器，那就方便多了
            .map(|v| v.to_digit(10).unwrap() as u8)
            .collect();
        let b: Vec<u8> = b
            .chars()
            .rev()
            .map(|v| v.to_digit(10).unwrap() as u8)
            .collect();

        let mut i = 0;
        let mut carry = 0;
        let mut res = vec![];

        while i < a.len() || i < b.len() {
            // 这样写比较优雅，不用管到底是a位数多还是b位数多
            let v = a.get(i).unwrap_or(&0); // 如果a位数不够了，就补0
            let w = b.get(i).unwrap_or(&0);

            match v + w + carry {
                0 => {
                    carry = 0;
                    res.push(0);
                }
                1 => {
                    carry = 0;
                    res.push(1);
                }
                2 => {
                    carry = 1;
                    res.push(0);
                }
                _ => {
                    carry = 1;
                    res.push(1);
                }
            };
            i += 1;
        }

        if carry == 1 {
            res.push(1);
        }

        return res
            .into_iter()
            .rev()
            .map(|v| std::char::from_digit(v, 10).unwrap())
            .collect();
    }
}

fn main() {
    dbg!(Solution::add_binary("11".into(), "1".into())); // 100
    dbg!(Solution::add_binary("1010".into(), "1011".into())); // 100
}
