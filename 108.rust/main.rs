// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
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
      right: None
    }
  }
}

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if (nums.is_empty()) {
            return None;
        } else {
            let length = nums.len();
            if (length == 1) {
                return Some(TreeNode {
                    val: *nums.get(length / 2).unwrap(),
                    left: None,
                    right: None,
                });
            } else {
                return Some(TreeNode {
                    val: *nums.get(length / 2).unwrap(),
                    left: Solution::sorted_array_to_bst(nums[0..length / 2].to_vec()),
                    right: Solution::sorted_array_to_bst(nums[length / 2 + 1..length].to_vec()),
                });
            }
        }
    }
}