struct Solution;

use std::collections::BinaryHeap;
use std::cmp::max;
use std::i32;

impl Solution {
    pub fn max_subarray_sum_circular(a: Vec<i32>) -> i32 {
        let mut integral = vec![0];

        for &v in a.iter().cycle().take(a.len() * 2) {
            let last = *integral.last().unwrap();
            integral.push(last + v);
        } // 实现py里的 integral = [0] + list(itertools.accumulate(a + a)) 但我总觉得rust应该也有类似的函数式写法吧

        // 确实有这种写法
        // integral.extend(
        //     a.iter()
        //     .cycle()
        //     .take(a.len() * 2)
        //     .scan(0, |state, &v| {
        //         *state = *state + v;
        //         return Some(*state);
        //     })
        // ); // 只想到了这种写法，但是不太容易用。

        let mut heap: BinaryHeap<(i32, usize)> = BinaryHeap::new(); // 注意是max heap，要存倒数
        heap.push(
            (0, 0)
        );
        let mut res = i32::MIN; // float("-inf")

        for (i, &v) in integral.iter().enumerate().skip(1) {
            
            while true {
                let smallest = heap.pop().unwrap();
                let (mut value, position) = smallest;
                value = 0 - value; // 存倒数真的不太方便
                if (position as i32) >= (i as i32) - (a.len() as i32) {
                    res = max(res, v - value);
                    heap.push((-value, position));
                    break;
                }
            }

            heap.push((-v, i));
        }

        return res;
    }
}

// pub fn main() {
//     println!("{:?}", Solution::max_subarray_sum_circular(vec![1, -2, 3, -2])); // 3
//     println!("{:?}", Solution::max_subarray_sum_circular(vec![5, -3, 5])); // 10
//     println!("{:?}", Solution::max_subarray_sum_circular(vec![-2, -3, -1])); // -1
// }