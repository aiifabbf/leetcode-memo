struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn get_no_zero_integers(n: i32) -> Vec<i32> {
        let allNonZeroIntegers: HashSet<i32> = (0..n).into_iter()
            .filter(|v| !v.to_string().contains("0"))
            .collect();

        for &v in allNonZeroIntegers.iter() {
            if allNonZeroIntegers.contains(&(n - v)) {
                return vec![v, n - v];
            }
        }

        return vec![0, 0];
    }
}

pub fn main() {
    println!("{:?}", Solution::get_no_zero_integers(2)); // [1, 1]
    println!("{:?}", Solution::get_no_zero_integers(11)); // [2, 9]
}