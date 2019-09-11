struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        match nums.len() {
            0 => vec![],
            1 => nums,
            2 => vec![*nums.iter().min().unwrap(), *nums.iter().max().unwrap()],
            _ => {
                let mut left: Vec<i32> = nums.iter().cloned().take(nums.len() / 2).collect();
                let mut right: Vec<i32> = nums.iter().cloned().skip(nums.len() / 2).collect();

                let mut left: VecDeque<i32> = VecDeque::from(Solution::sort_array(left));
                let mut right: VecDeque<i32> = VecDeque::from(Solution::sort_array(right));
                let mut res = vec![];

                while (!left.is_empty()) && (!right.is_empty()) {
                    if left[0] > right[0] {
                        res.push(right.pop_front().unwrap());
                    } else {
                        res.push(left.pop_front().unwrap());
                    }
                }

                if left.is_empty() {
                    res.append(&mut right.iter().cloned().collect::<Vec<i32>>());
                } else {
                    res.append(&mut left.iter().cloned().collect::<Vec<i32>>());
                }

                res
            }
        }
    }
}

// pub fn main() {
//     println!("{:?}", Solution::sort_array(vec![5, 2, 3, 1]));
//     println!("{:?}", Solution::sort_array(vec![5, 1, 1, 2, 0, 0]));
// }