/*
矩阵里最大的全1子方阵

老掉牙的题了，二维积分。设 ``integrals[i][j]`` 是子矩阵 ``M[: i][: j]`` 的累加和。这样任意子矩阵的累加和可以很方便地算出来。
*/

struct Solution;

use std::cmp::max;
use std::cmp::min;

impl Solution {
    pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() {
            return 0;
        }

        let rowCount = matrix.len();
        let columnCount = matrix[0].len();
        let mut integrals = vec![vec![0; columnCount + 1]; rowCount + 1];

        let mut res = 0;

        for i in 1..rowCount + 1 {
            for j in 1..columnCount + 1 {
                integrals[i][j] = matrix[i - 1][j - 1].to_digit(10).unwrap() as usize
                    + integrals[i - 1][j]
                    + integrals[i][j - 1]
                    - integrals[i - 1][j - 1];

                for delta in 1..min(i, j) + 1 {
                    // 看看子方阵M[i - delta: i][j - delta: j]里是不是全1
                    if integrals[i][j] + integrals[i - delta][j - delta]
                        - integrals[i][j - delta]
                        - integrals[i - delta][j]
                        == delta.pow(2)
                    {
                        // 判断是不是全1很好办，看子矩阵累加和是不是正好就是边长的平方就好了
                        res = max(res, delta.pow(2));
                    }
                }
            }
        }

        println!("{:?}", integrals);

        return res as i32;
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::maximal_square(vec![
            vec!['1', '0', '1', '0', '0'],
            vec!['1', '0', '1', '1', '1'],
            vec!['1', '1', '1', '1', '1'],
            vec!['1', '0', '0', '1', '0'],
        ])
    ); // 4
    println!("{:?}", Solution::maximal_square(vec![vec!['1'],])); // 1
}
