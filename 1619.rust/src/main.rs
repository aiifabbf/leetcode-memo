/*
.. default-role:: math

去掉array最小和最大的5%，计算剩下的数的平均数。

.. 这周没做双周赛。
*/

struct Solution;

impl Solution {
    pub fn trim_mean(arr: Vec<i32>) -> f64 {
        let mut array = arr;
        array.sort();
        let length = array.len();

        return array
            .into_iter()
            .skip(length / 20)
            .take(length - length / 10)
            // .sum::<i32>() as f64 // 我有点担心它会溢出……
            .fold(0_isize, |acc, v| acc + v as isize) as f64
            / (length - length / 10) as f64;
    }
}

fn main() {
    dbg!(Solution::trim_mean(vec![
        1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3
    ])); // 2
    dbg!(Solution::trim_mean(vec![
        6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0
    ])); // 4
    dbg!(Solution::trim_mean(vec![
        6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8,
        6, 6, 1, 0, 6, 10, 8, 2, 3, 4
    ])); // 4.777..
}
