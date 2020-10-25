/*
.. default-role:: math

二分搜索

试着用递归写了一下，看起来真的赏心悦目，太舒服了……
*/

struct Solution;

use std::cmp::Ordering;

impl Solution {
    // 老套的迭代写法
    #[cfg(feature = "imperative")]
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        if nums.len() == 0 {
            return -1;
        }

        let mut left = 0;
        let mut right = nums.len();

        while left < right {
            let middle = left + (right - left) / 2; // 为了避免left + right溢出。讲道理usize + usize能有多大几率溢出呢，地球上所有的数据量加起来都没有2^63字节吧
            if nums[middle] == target {
                return middle as i32;
            } else if nums[middle] < target {
                left = middle + 1;
            } else if nums[middle] > target {
                right = middle;
            }
        }

        if 0 <= left && left < nums.len() {
            if nums[left] == target {
                return left as i32;
            } else {
                return -1;
            }
        } else {
            return -1;
        }
    }

    // 极为先进的函数式
    #[cfg(feature = "functional")]
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let index = Self::binary_search_left(&nums[..], target);

        match nums.get(index) {
            Some(v) if *v == target => index as i32,
            _ => -1,
        }
    }

    // 看起来真是赏心悦目啊。根本不用担心stack overflow之类的问题，因为最大深度就ln n
    // 纠结了一下要不要改成泛型，不改了，改起来就没完没了了，比如target要不要改成&T呢？target的类型能不能不要限定的那么死呢，能不能是另一个类型、但是能和array里的元素比大小呢
    fn binary_search_left(array: &[i32], target: i32) -> usize {
        let middle = (0 + array.len()) / 2;

        match array.get(middle) {
            Some(v) => match target.cmp(v) {
                Ordering::Equal => Self::binary_search_left(&array[..middle], target),
                Ordering::Less => Self::binary_search_left(&array[..middle], target),
                Ordering::Greater => {
                    middle + 1 + Self::binary_search_left(&array[middle + 1..], target)
                }
            },
            _ => 0,
        }
    }
}

fn main() {
    dbg!(Solution::search(vec![-1, 0, 3, 5, 9, 12], 9)); // 4
    dbg!(Solution::search(vec![-1, 0, 3, 5, 9, 12], 2)); // -1
}
