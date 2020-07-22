struct Solution;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn zigzag_level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        if let Some(root) = root {
            let mut queue = vec![root];
            let mut res = vec![];
            let mut sequence = true; // true表示从左到右

            while !queue.is_empty() {
                let mut newQueue = vec![];
                let mut level = vec![]; // 这一层节点的值

                for node in queue.iter() {
                    if let Some(node) = node.borrow().left.clone() {
                        // 遇事不决就clone
                        newQueue.push(node);
                    }
                    if let Some(node) = node.borrow().right.clone() {
                        newQueue.push(node);
                    }
                    level.push(node.borrow().val);
                }

                if sequence == false {
                    // 如果这一层需要从右往左
                    level.reverse();
                }
                sequence = !sequence;
                res.push(level);

                queue = newQueue;
            }

            return res;
        } else {
            return vec![];
        }
    }
}

fn main() {}
