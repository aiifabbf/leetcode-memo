struct Solution;

impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, arr2: Vec<i32>, d: i32) -> i32 {
        let mut res = 0;

        for v in arr1.iter() {
            if !arr2.iter().any(|w| (v - w).abs() <= d) { // rust也有any好评
                res += 1;
            }
        }

        return res;
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::find_the_distance_value(vec![4, 5, 8], vec![10, 9, 1, 8], 2)
    ); // 2
}
