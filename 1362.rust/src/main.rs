struct Solution;

impl Solution {
    pub fn closest_divisors(num: i32) -> Vec<i32> {
        let a = Solution::divisors(num + 1);
        let b = Solution::divisors(num + 2);

        return vec![a, b]
            .into_iter()
            .min_by_key(|v| (v[0] - v[1]).abs())
            .unwrap();
    }

    fn divisors(num: i32) -> Vec<i32> {
        let mut res: Vec<i32> = vec![1, num];

        for i in 1..((num as f64).sqrt().ceil() as i32) + 1 {
            if num % i == 0 {
                res = vec![i, num / i];
            }
        }

        return res;
    }
}

pub fn main() {
    println!("{:?}", Solution::closest_divisors(8)); // [3, 3]
    println!("{:?}", Solution::closest_divisors(123)); // [5, 25]
}
