struct Solution;

use std::cmp::max;

impl Solution {
    pub fn min_flips(a: i32, b: i32, c: i32) -> i32 {
        let mut a: Vec<char> = format!("{:b}", a).chars().collect();
        let mut b: Vec<char> = format!("{:b}", b).chars().collect();
        let mut c: Vec<char> = format!("{:b}", c).chars().collect();
        a.reverse();
        b.reverse();
        c.reverse();
        let length: i32 = vec![&a, &b, &c].iter()
            .map(|v| v.len())
            .max()
            .unwrap() as i32;
        (0..max(0, length - a.len() as i32))
            .for_each(|v| a.push('0'));
        (0..max(0, length - b.len() as i32))
            .for_each(|v| b.push('0'));
        (0..max(0, length - c.len() as i32))
            .for_each(|v| c.push('0')); // 补零

        let mut res: i32 = 0;

        for (i, &v) in c.iter().enumerate() {
            match(v) { // 用match还是比if好看多了。
                '0' => {
                    match(a[i], b[i]) {
                        ('1', '1') => {res += 2},
                        ('1', '0') => {res += 1},
                        ('0', '1') => {res += 1},
                        _ => {},
                    };
                },
                '1' => {
                    match(a[i], b[i]) {
                        ('0', '0') => {res += 1},
                        _ => {},
                    };
                },
                _ => {},
            };
        }

        return res;
    }
}

pub fn main() {
    println!("{:?}", Solution::min_flips(2, 6, 5)); // 3
    println!("{:?}", Solution::min_flips(4, 2, 7)); // 1
}