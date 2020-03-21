struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn max_number_of_families(n: i32, reserved_seats: Vec<Vec<i32>>) -> i32 {
        let mut reserved = HashMap::new();

        for v in reserved_seats.iter() {
            let rowIndex = v[0];
            let columnIndex = v[1];
            reserved
                .entry(rowIndex)
                .or_insert(HashSet::new())
                .insert(columnIndex);
        }

        let mut res = (n as usize - reserved.len()) * 2;

        for (_, row) in reserved.iter() {
            let left;
            let right;
            let middle;

            if [2, 3, 4, 5].iter().any(|v| row.contains(v)) {
                left = false;
            } else {
                left = true;
            }

            if [6, 7, 8, 9].iter().any(|v| row.contains(v)) {
                right = false;
            } else {
                right = true;
            }

            if [4, 5, 6, 7].iter().any(|v| row.contains(v)) {
                middle = false;
            } else {
                middle = true;
            }

            match (left, right) {
                (true, true) => {
                    res += 2;
                }
                (true, false) => {
                    res += 1;
                }
                (false, true) => {
                    res += 1;
                }
                (false, false) => {
                    if middle {
                        res += 1;
                    }
                }
            }
        }
        return res as i32;
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::max_number_of_families(
            3,
            vec![
                vec![1, 2],
                vec![1, 3],
                vec![1, 8],
                vec![2, 6],
                vec![3, 1],
                vec![3, 10]
            ]
        )
    ); // 4
}
