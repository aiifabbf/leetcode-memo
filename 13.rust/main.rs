struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let table: HashMap<char, i32> = vec![
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ].iter().cloned().collect();

        let mut iterator = s.chars();
        let mut res = *table.get(&iterator.next().unwrap()).unwrap();
        let mut last = res;

        for v in iterator.map(|v| *table.get(&v).unwrap()) {
            if last < v {
                res = res + v - 2 * last;
            } else {
                res = res + v;
            }
            last = v;
        }

        return res;
    }
}

// pub fn main() {
//     println!("{}", Solution::roman_to_int("III".to_string())); // 3
//     println!("{}", Solution::roman_to_int("IV".to_string())); // 4
//     println!("{}", Solution::roman_to_int("LVIII".to_string())); // 58
// }