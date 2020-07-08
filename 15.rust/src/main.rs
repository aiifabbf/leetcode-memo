struct Solution;

use std::cmp::min;
use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut counter = HashMap::new();

        for v in nums.iter() {
            if let Some(count) = counter.get_mut(v) {
                *count = min(*count + 1, 3);
            } else {
                counter.insert(*v, 1);
            }
        }

        let mut nums = vec![];

        for (k, v) in counter.into_iter() {
            for _ in 0..v {
                nums.push(k);
            }
        }

        let mut res = HashSet::new();

        for (i, v) in nums.iter().enumerate() {
            let twoSums = Solution::two_sum(&nums[i + 1..], 0 - *v);
            for w in twoSums.iter() {
                let mut triplet = [*v, w[0], w[1]];
                triplet.sort();
                res.insert(triplet);
            }
        }

        return res.into_iter().map(|v| Vec::from(&v[..])).collect();
    }

    fn two_sum(nums: &[i32], target: i32) -> HashSet<[i32; 2]> {
        let mut res = HashSet::new();
        let mut seen = HashSet::new();

        for v in nums.iter() {
            if seen.contains(&(target - *v)) {
                let mut pair = [target - *v, *v];
                pair.sort();
                res.insert(pair);
            }
            seen.insert(*v);
        }

        return res;
    }
}

fn main() {
    println!("{:#?}", Solution::three_sum(vec![-1, 0, 1, 2, -1, -4])); // [[-1, 0, 1], [-1, -1, 2]]
}
