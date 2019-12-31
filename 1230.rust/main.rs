struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn probability_of_heads(prob: Vec<f64>, target: i32) -> f64 {
        let mut dp: HashMap<(i32, i32), f64> = HashMap::new();
        let length: i32 = prob.len() as i32;

        dp.insert((0, 0), 1.0);

        for t in 1..(target + 1) {
            dp.insert((0, t), 0.0);
        }

        for k in 1..(length + 1) {
            dp.insert((k, 0), *dp.get(&(k - 1, 0)).unwrap() * (1 as f64 - *prob.get(k as usize - 1).unwrap()));
        }

        for k in 1..(length + 1) {

            for t in 1..(target + 1) {
                dp.insert((k, t), *prob.get(k as usize - 1).unwrap() * *dp.get(&(k - 1, t - 1)).unwrap() + (1 as f64 - *prob.get(k as usize - 1).unwrap()) * *dp.get(&(k - 1, t)).unwrap());
            }

        }

        return *dp.get(&(length, target)).unwrap();
    }
}

pub fn main() {
    println!("{:?}", Solution::probability_of_heads(vec![0.5, 0.5, 0.5, 0.5, 0.5], 0));
}