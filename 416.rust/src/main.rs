struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let summation: i32 = nums.iter().sum();
        if summation % 2 != 0 {
            // 如果整个集合的和是奇数的话，和的一半一定是个xxx.5，因为集合里的数又都是整数，所以子集凑成的和肯定也是整数，无论如何都不可能凑到xxx.5这种数。所以可以直接false掉
            return false;
        }
        let target: i32 = summation / 2;
        let mut summations: HashSet<i32> = HashSet::with_capacity(target as usize + 1);

        for v in nums.iter() {
            let mut newSummations: HashSet<i32> = HashSet::with_capacity(target as usize + 1);
            newSummations.insert(*v);

            for w in summations.iter() {
                if (*v + *w) <= target {
                    newSummations.insert(*v + *w);
                }
            }

            summations.extend(newSummations.into_iter());
            if summations.contains(&target) {
                return true;
            }
        }

        return false;
    }
}

pub fn main() {
    println!("{:?}", Solution::can_partition(vec![1, 5, 11, 5])); // true
    println!("{:?}", Solution::can_partition(vec![1, 2, 3, 5])); // false
}
