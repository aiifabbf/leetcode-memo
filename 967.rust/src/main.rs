/*
.. default-role:: math

列出所有十进制 `n` 位数，并且每个数字任意相邻两位差值的绝对值正好是 `k`

比如所有任意相邻两位差值绝对值正好是7的3位数有

::

    181, 292, 707, 818, 929
                        --
                         -- 任意相邻两位差值的绝对值是7

用回溯挺好的。每次要做选择的时候，看一下选择的这个数字和上一个数字的差值是否满足条件，如果满足，就试一下填这个数字，再进入下一层。
*/

struct Solution;

impl Solution {
    pub fn nums_same_consec_diff(n: i32, k: i32) -> Vec<i32> {
        let mut path = vec![];
        let mut res = vec![];
        Self::backtrack(&mut path, n as usize, k, &mut res);
        return res
            .into_iter()
            .map(|v| v.into_iter().fold(0, |acc, v| acc * 10 + v)) // 把[2, 9, 2]变成292
            .collect();
    }

    fn backtrack(path: &mut Vec<i32>, length: usize, difference: i32, res: &mut Vec<Vec<i32>>) {
        if path.len() == length {
            // 已经是3位数了，够了
            res.push(path.clone()); // 加入到结果集
        } else {
            if path.is_empty() {
                let start = if length == 1 { 0 } else { 1 }; // 0不能做首位，不然会出现070这种，所以这里判断一下，如果只要1位数，那么0可以算进来，如果是2位数，第一位就不能是0了

                for i in start..10 {
                    path.push(i);
                    Self::backtrack(path, length, difference, res);
                    path.pop();
                }
            } else {
                for i in 0..10 {
                    if (path.last().unwrap().clone() - i).abs() == difference {
                        // 这个数字和前一位的差值的绝对值满足要求
                        path.push(i); // 这一位用这个数字试一下
                        Self::backtrack(path, length, difference, res);
                        path.pop(); // 撤销
                    }
                }
            }
        }
    }
}

fn main() {
    dbg!(Solution::nums_same_consec_diff(3, 7)); // 181, 292, 707, 818 929
    dbg!(Solution::nums_same_consec_diff(2, 1)); // 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98
    dbg!(Solution::nums_same_consec_diff(1, 0)); //
}
