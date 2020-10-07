/*
.. default-role:: math

往二分搜索树里插入数字

用Rust写了同款，同样的配方、同样的味道、同样的immutable和递归，性能应该很差吧……但看起来真的赏心悦目。
*/

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
    pub fn insert_into_bst(
        root: Option<Rc<RefCell<TreeNode>>>,
        val: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        match root {
            Some(node) => {
                if val < node.borrow().val {
                    Some(Rc::new(RefCell::new(TreeNode {
                        val: node.borrow().val,
                        left: Solution::insert_into_bst(node.borrow().left.clone(), val),
                        right: node.borrow().right.clone(),
                    }))) // 看起来非常函数式，但是性能应该很差吧……
                } else if val > node.borrow().val {
                    Some(Rc::new(RefCell::new(TreeNode {
                        val: node.borrow().val,
                        left: node.borrow().left.clone(),
                        right: Solution::insert_into_bst(node.borrow().right.clone(), val),
                    })))
                } else {
                    None
                }
            }
            None => Some(Rc::new(RefCell::new(TreeNode::new(val)))),
        }
    }
}

fn main() {
    dbg!(Solution::insert_into_bst(
        Some(Rc::new(RefCell::new(TreeNode {
            val: 4,
            left: Some(Rc::new(RefCell::new(TreeNode {
                val: 2,
                left: Some(Rc::new(RefCell::new(TreeNode {
                    val: 1,
                    left: None,
                    right: None,
                }))),
                right: Some(Rc::new(RefCell::new(TreeNode {
                    val: 3,
                    left: None,
                    right: None,
                }))),
            }))),
            right: Some(Rc::new(RefCell::new(TreeNode {
                val: 7,
                left: None,
                right: None,
            })))
        }))),
        5
    ));
}
