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

use std::collections::VecDeque;

impl Solution {
    pub fn width_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if let Some(root) = root {
            let mut queue: VecDeque<(Rc<RefCell<TreeNode>>, u64)> = VecDeque::new();
            queue.push_back((root, 0));
            let mut res = 1;

            while !queue.is_empty() {
                res = res.max(queue.back().unwrap().1 - queue.front().unwrap().1 + 1);

                for _ in 0..queue.len() {
                    let (node, number) = queue.pop_front().unwrap();

                    if let Some(node) = &node.borrow().left {
                        queue.push_back((node.clone(), number * 2));
                    }

                    if let Some(node) = &node.borrow().right {
                        queue.push_back((node.clone(), number * 2 + 1));
                    };
                }
            }

            return res as i32;
        } else {
            return 0;
        }
    }
}

fn main() {}
