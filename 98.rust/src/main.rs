/*
验证二叉树是不是二分搜索树。

最简单的方法，利用“二分搜索树的中根遍历严格递增”和“二叉树是二分搜索”互为充要条件的性质，直接看中根遍历是不是严格递增就好了。

.. 我第一次知道这两个居然是充要条件也是很震惊的。印象中总觉得BST是个更强的条件。
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
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let inorder = Solution::inorderTraversal(&root); // 得到中根遍历

        for (i, v) in inorder.iter().enumerate().skip(1) {
            if v.clone() <= inorder[i - 1] {
                // 如果不是严格递增
                return false; // 肯定不是二分搜索树
            }
        }

        return true; // 否则就是二分搜索树
    }

    fn inorderTraversal(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        if let Some(inner) = root.as_ref() {
            let mut res = Solution::inorderTraversal(&inner.borrow().left);
            res.push(inner.borrow().val);
            res.extend(Solution::inorderTraversal(&inner.borrow().right).into_iter());
            return res;
        } else {
            return vec![];
        }
    }
}

fn main() {}
