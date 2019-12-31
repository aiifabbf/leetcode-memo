struct Solution;

use std::cmp::Ordering;

impl Solution {
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
        let a: i32 = coordinates[0].clone();
        let b: i32 = coordinates[1].clone();
        let slope: f64 = (b[1] - a[1]) as f64 / (b[0] - a[0]) as f64; // 不用管除零错误，因为在rust里除零会得到inf

        for (_, v) in coordinates.iter().skip(1).enumerate() {
            let thisSlope: f64 = (v[1] - a[1]) as f64 / (v[0] - a[0]) as f64;

            match thisSlope.partial_cmp(&slope) { // 比较恶心（也不能叫恶心，应该叫严谨）的是，rust里面float是不能直接比大小的，因为rust认为float里存在nan，这个nan和任何float都不相等，所以float集合不是一个total ordering，而是一个partial ordering。所以要用.partial_cmp()来比较大小
                Some(Ordering::Equal) => {
                    continue;
                },
                _ => {
                    return false;
                }
            };

        }

        return true;
    }
}

pub fn main() {
    println!("{:?}", Solution::check_straight_line(vec![vec![1, 2], vec![2, 3]])); // true
}