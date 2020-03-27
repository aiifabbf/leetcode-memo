/* 
详细解释在 `python版 <./239.py>`_ 里。
*/

struct Solution;

trait Decreasing<T: Ord> {
    // 可以玩一下……给VecDeque实现单调非严格递减queue的性质
    fn push_back_decreasing(&mut self, value: T);
}

use std::collections::BinaryHeap;
use std::collections::VecDeque;

impl Solution {
    // 用单调队列的做法就是我没法自发想到的了……
    #[cfg(feature = "monotonous-queue")]
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        if nums.len() == 0 {
            return vec![];
        }

        let mut queue = VecDeque::new(); // 是个单调非严格递减queue

        for i in 0..k as usize {
            // 初始化初始窗口
            if queue.is_empty() {
                queue.push_back((nums[i], i));
            } else {
                while !queue.is_empty() {
                    if queue.back().cloned().unwrap().0 < nums[i] {
                        // 最后一个元素比当前元素小才会比踢出去，和当前元素一样大的话会被保留在queue里
                        queue.pop_back();
                    } else {
                        break;
                    }
                }

                queue.push_back((nums[i], i));
            }
        }
        // 可以看到初始化窗口比heap的烦多了……而且下面滑动的时候还要再写一遍

        // println!("{:?}", queue); // 这样出来之后，queue就是个单调非严格递减的了

        let mut res = vec![queue.front().cloned().unwrap().0]; // queue的第一个元素就是初始窗口里最大的元素啦

        for i in 1..(nums.len() - k as usize + 1) {
            // 开始滑滑乐。添加新元素，新元素位于i - 1 + k。
            // 为什么新元素位于i - 1 + k呢，因为指针现在虽然已经指到i了，但是窗口还是在[i - 1, i - 1 + k)那里，新的窗口应该是[i, i + k)，所以需要添加nums[i - 1 + k]这个元素
            while !queue.is_empty() {
                if queue.back().cloned().unwrap().0 < nums[i - 1 + k as usize] {
                    // 维持单调非严格递减性质
                    queue.pop_back();
                } else {
                    break;
                }
            }

            queue.push_back((nums[i - 1 + k as usize], i - 1 + k as usize));

            while !queue.is_empty() {
                if queue.front().cloned().unwrap().1 < i {
                    // 队列第一个元素虽然是最大的，可是它并不在当前窗口啊
                    queue.pop_front(); // 所以只能扔掉
                } else {
                    // 一旦发现了第一个在当前窗口的元素
                    break; // 这个元素铁定是当前窗口里最大的元素
                }
            }

            // println!("{:?}", queue);

            res.push(queue.front().cloned().unwrap().0);
        }

        return res;
    }

    // 用heap的做法，是我自发能想到的做法
    #[cfg(feature = "heap")]
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        if nums.len() == 0 {
            return vec![];
        } else {
            let mut heap = BinaryHeap::new();

            for i in 0..k {
                heap.push((nums[i as usize], i)); // 初始窗口
            }

            let mut res = vec![heap.peek().cloned().unwrap().0]; // 前k个里面的最大值

            for i in 1..(nums.len() as i32 - k + 1) {
                // 这里我突然不知道怎么改成进入for之后窗口就是正确的，怎么改成后处理？
                // 只能前处理了
                heap.push((nums[(i + k - 1) as usize], i + k - 1)); // 新窗口[1, k + 1)

                while true {
                    let (maximum, index) = heap.pop().unwrap();
                    if index >= i {
                        heap.push((maximum, index)); // 放回
                        res.push(maximum);
                        break;
                    } // index < i的直接扔掉，不用放回
                }
            }

            return res;
        }
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::max_sliding_window(vec![1, 3, -1, -3, 5, 3, 6, 7], 3)
    ); // [3, 3, 5, 5, 6, 7]
}
