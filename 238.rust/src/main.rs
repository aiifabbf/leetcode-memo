struct Solution;

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let productBefore: Vec<i32> = vec![1]
            .into_iter()
            .chain(nums.iter().scan(1, |state, v| {
                *state = *state * *v;
                return Some(*state);
            }))
            .collect();

        let mut productAfter: Vec<i32> = vec![1]
            .into_iter()
            .chain(nums.iter().rev().scan(1, |state, v| {
                *state = *state * *v;
                return Some(*state);
            }))
            // .rev() // 这里不支持rev()，因为chain不是DoubleEndedIterator
            .collect();

        productAfter.reverse();

        return nums
            .iter()
            .enumerate()
            .map(|(i, _)| {
                return productBefore[i] * productAfter[i + 1];
            })
            .collect(); // 这里不用写collect::<Vec<i32>>()，会自动根据函数返回值类型推断
    }
}

pub fn main() {
    println!("{:?}", Solution::product_except_self(vec![1, 2, 3, 4])); // 24, 12, 8, 6
}
