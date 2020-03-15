/*
.. default-role:: math

实现stack，同时还要实现 `O(1)` 得到stack里最小的元素。

这个简单，另外用一个list存至今为止见过的最小的元素就好了。
*/

struct MinStack {
    stack: Vec<i32>,
    cumulativeMinimum: Vec<i32>, // 至今为止见过的最小的元素
}

use std::cmp::min;

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {
    /** initialize your data structure here. */
    fn new() -> Self {
        return MinStack {
            stack: vec![],
            cumulativeMinimum: vec![],
        };
    }

    fn push(&mut self, x: i32) {
        self.stack.push(x);
        if self.cumulativeMinimum.is_empty() {
            self.cumulativeMinimum.push(x);
        } else {
            self.cumulativeMinimum
                .push(min(x, self.cumulativeMinimum.last().cloned().unwrap()));
        }
    }

    fn pop(&mut self) {
        self.stack.pop();
        self.cumulativeMinimum.pop();
    }

    fn top(&self) -> i32 {
        return self.stack.last().cloned().unwrap();
    }

    fn get_min(&self) -> i32 {
        return self.cumulativeMinimum.last().cloned().unwrap();
    }
}

pub fn main() {}
