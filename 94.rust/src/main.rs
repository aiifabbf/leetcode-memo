/*
.. default-role:: math

中根遍历二叉树

用Rust又写了一遍，递归和迭代都写了。详细解释在Python写的版本里。
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
    #[cfg(feature = "recursive")]
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        match root {
            Some(v) => {
                let mut res: Vec<i32> = Vec::new();
                res.extend(
                    &mut Solution::inorder_traversal(v.borrow().left.clone())
                        .iter()
                        .cloned(),
                );
                res.push(v.borrow().val);
                res.extend(
                    &mut Solution::inorder_traversal(v.borrow().right.clone())
                        .iter()
                        .cloned(),
                );
                return res;
            }
            None => {
                return vec![];
            }
        }
    }

    #[cfg(feature = "iterative")]
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        if let Some(root) = root {
            let mut stack = vec![];
            let mut res = vec![];
            let mut head = root.clone(); // 不知道怎么改成&
            let mut pc = 0;

            loop {
                match pc {
                    0 => {
                        if let Some(left) = &head.clone().borrow().left {
                            // 如果存在左边子树
                            pc = 1;
                            stack.push((head, pc)); // 暂存当前函数帧

                            // 然后调用遍历左边子树的函数
                            head = left.clone();
                            pc = 0;
                        } else {
                            // 如果不存在
                            pc = 1; // 啥也不做，goto第二段程序
                        }
                    }
                    1 => {
                        // 如果有左边子树，那么刚才已经遍历过左边子树了；如果没有左边子树，那么刚才什么都没做，不管怎样，现在应该遍历当前节点了
                        res.push(head.borrow().val);
                        if let Some(right) = &head.clone().borrow().right {
                            // 如果存在右边子树
                            pc = 2;
                            stack.push((head, pc)); // 同样暂存当前函数帧

                            // 然后调用遍历右边子树的函数
                            head = right.clone();
                            pc = 0;
                        } else {
                            pc = 2;
                        }
                    }
                    2 => {
                        // 左边、根节点、右边子树全部都已经遍历过了
                        if let Some(frame) = stack.pop() {
                            // 此时应该返回上一层
                            head = frame.0;
                            pc = frame.1;
                        } else {
                            // 如果没有上一层
                            break;
                        }
                    }
                    _ => {}
                }
            }

            return res;
        } else {
            return vec![];
        }
    }
}

fn main() {
    dbg!(Solution::inorder_traversal(Some(Rc::new(RefCell::new(
        TreeNode {
            val: 1,
            left: None,
            right: Some(Rc::new(RefCell::new(TreeNode {
                val: 2,
                left: Some(Rc::new(RefCell::new(TreeNode {
                    val: 3,
                    left: None,
                    right: None,
                }))),
                right: None,
            })))
        }
    ))))); // [1, 3, 2]
}
