/* 
用rust试着写了一下two sum，还是不错的。

不过每次提交之前都要先把 ``main()`` 和最前面的 ``struct Solution`` 注释掉，有点恶心。
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();
        
        for (i, &v) in nums.iter().enumerate() {
            if seen.contains_key(&(target - v)) {
                return vec![*seen.get(&(target - v)).unwrap(), i as i32];
            } else {
                seen.insert(v, i as i32);
            }
        }

        return vec![];
    }
}

// pub fn main() {
//     println!("{:?}", Solution::two_sum(vec![2, 7, 11, 15], 9)); // [0, 1]
// }