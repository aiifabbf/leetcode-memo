/* 
把从小到大排好序的array变成平衡二分搜索树。

很简单，如果只有一个元素，那就这个节点了。如果有多个元素，取出最中间的那个元素作为根节点，前面的元素递归地建一个BST、后面的元素也递归地建一个BST。

更详细的解释在python版里。
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
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        return Solution::sortedArrayToBst(&nums[..]);
    }
    fn sortedArrayToBst(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
        if nums.is_empty() {
            return None;
        } else {
            let length = nums.len();
            if length == 1 {
                // 只有一个元素
                return Some(Rc::new(RefCell::new(TreeNode {
                    val: nums[length / 2],
                    left: None,
                    right: None,
                })));
            } else {
                // 有多个元素
                return Some(Rc::new(RefCell::new(TreeNode {
                    val: nums[length / 2], // 最中间那个作为根节点
                    left: Solution::sortedArrayToBst(&nums[0..length / 2]), // 前面的元素建一个BST
                    right: Solution::sortedArrayToBst(&nums[length / 2 + 1..length]), // 后面的元素建一个BST
                })));
            }
        }
    }
}

fn main() {
    println!("{:#?}", Solution::sorted_array_to_bst(vec![-10, -3, 0, 5, 9]));
}
