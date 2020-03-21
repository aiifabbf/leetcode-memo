struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn get_kth(lo: i32, hi: i32, k: i32) -> i32 {
        let mut cache = HashMap::new(); // 可惜rust没有functools.lru_cache，也没有装饰器

        for i in 1..1001 {
            if !cache.contains_key(&i) {
                cache.insert(i, Solution::power(i));
            }
        }

        let mut array: Vec<i32> = (lo..hi + 1).collect();
        array.sort_by_key(|v| (cache[v], *v));

        return array[k as usize - 1];
    }

    fn power(n: i32) -> i32 {
        if n == 1 {
            return 1;
        } else if n % 2 == 0 {
            return 1 + Solution::power(n / 2);
        } else {
            return 1 + Solution::power(3 * n + 1);
        }
    }
}

fn main() {
    println!("{:?}", Solution::get_kth(12, 15, 2)); // 7
    println!("{:?}", Solution::get_kth(1, 1, 1)); // 1
    println!("{:?}", Solution::get_kth(7, 11, 4)); // 7
    println!("{:?}", Solution::get_kth(10, 20, 5)); // 13
    println!("{:?}", Solution::get_kth(1, 1000, 777)); // 570
}
