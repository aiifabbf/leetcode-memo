/*
.. default-role:: math

算出Pascal三角形的第 `i` 行

第一反应就是一行一行算，从第 `i - 1` 行算出第 `i` 行。

也可以直接用数学方法算，第 `i` 行第 `j` 个元素是 `C_i^j` 。
*/

struct Solution;

impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        if row_index == 0 {
            return vec![1];
        } else if row_index == 1 {
            return vec![1, 1];
        } else {
            let mut last = vec![1, 1];

            for i in 2..row_index + 1 {
                // 算出第i层
                let mut level = vec![1; last.len() + 1];

                for j in 1..level.len() - 1 {
                    // 的第j个元素
                    level[j] = last[j - 1] + last[j];
                }

                last = level;
            }

            return last;
        }
    }
}

fn main() {
    dbg!(Solution::get_row(3)); // [1, 3, 3, 1]
}
