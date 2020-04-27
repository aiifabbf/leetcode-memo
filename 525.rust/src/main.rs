/*
给一个array，问这个array里含有等量0和1的最长substring（要连续）的长度是多少。

把所有0都变成-1，问题就转换成了求累加和为0的最长substring的长度。然后又是喜闻乐见的积分/前缀和了。
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn find_max_length(nums: Vec<i32>) -> i32 {
        let length = nums.len();
        let integrals: Vec<i32> = vec![0]
            .into_iter()
            .chain(nums.into_iter().scan(0, |state, v| {
                if v == 0 {
                    // 把0都当做-1
                    *state = *state - 1;
                } else {
                    *state = *state + 1;
                }
                return Some(*state);
            }))
            .collect();

        let mut res = 0;
        let mut seen = HashMap::new(); // key是积分值，value是这个积分值第一次出现的下标

        for j in 0..length + 1 {
            match seen.get(&integrals[j]) {
                Some(i) => {
                    res = res.max(j - i);
                }
                None => {
                    seen.insert(integrals[j], j);
                }
            }
        }

        return res as i32;
    }
}

fn main() {
    println!("{:?}", Solution::find_max_length(vec![0, 1])); // 2
    println!("{:?}", Solution::find_max_length(vec![0, 1, 0])); // 2
}
