/* 
一个二分搜索树里面有两个元素被对调了位置。把这个二分搜索树恢复成原来的样子。

BST的inorder遍历会得到从小到大排好序的array，所以啥也别管，直接先inorder一遍，会得到一个array，当然因为对调位置，这个array不是排好序的了。

去这个array里面找顺序不对的元素。怎么找呢？最暴力的就是，先把array排序一下，然后和原来的array逐个对比，出现不一样的说明被对调了。

比如 ``2, 1, 3, 4, 5`` 排好序之后变成 ``1, 2, 3, 4, 5`` ，放在一起对比一下

::

    2, 1, 3, 4, 5
    1, 2, 3, 4, 5

很容易发现1和2被对调了。

既然已经找到对调的元素了，那就到原来的BST里面找到这两个节点，然后把这两个节点的值交换一下就好了。

评论区有人说Morris遍历，这个好像不需要额外空间。不过好难，没看。
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

use std::collections::HashSet;
use std::collections::VecDeque;

impl Solution {
    pub fn recover_tree(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        if root.is_none() {
            return;
        }

        let inorder = Solution::inorderTraversal(&root); // 啥也别管，先inorder遍历一遍
        let mut sortedInorder = inorder.clone();
        sortedInorder.sort(); // 排序
        let mut targets = HashSet::new();

        for v in inorder.iter().zip(sortedInorder.iter()) {
            // 一个一个对比
            if v.0 != v.1 {
                // 发现不一样的
                targets.insert(v.0.clone()); // 说面这个元素出现的位置不对，肯定是被对调了
            }
        }

        let mut nodes = vec![];
        let mut queue = VecDeque::new(); // 然后BFS找到这两个值对应的节点
        queue.push_back(root.clone());

        while !queue.is_empty() {
            let node = queue.pop_front().unwrap();
            if node.as_ref().unwrap().borrow().left.is_some() {
                queue.push_back(node.as_ref().unwrap().borrow().left.clone());
            }
            if node.as_ref().unwrap().borrow().right.is_some() {
                queue.push_back(node.as_ref().unwrap().borrow().right.clone());
            }
            if targets.contains(&node.as_ref().unwrap().borrow().val) {
                // 找到了
                nodes.push(node);
            }
        }

        let a = nodes.get(0).unwrap().clone();
        let b = nodes.get(1).unwrap().clone();

        std::mem::swap(&mut a.as_ref().unwrap().borrow_mut().val, &mut b.as_ref().unwrap().borrow_mut().val); // 交换这两个节点的值
    }

    fn inorderTraversal(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        if root.is_none() {
            return vec![];
        } else {
            let mut res = vec![];
            let leftInorder = Solution::inorderTraversal(&root.as_ref().unwrap().borrow().left);
            let rightInorder = Solution::inorderTraversal(&root.as_ref().unwrap().borrow().right);

            res.extend(leftInorder.into_iter());
            res.push(root.as_ref().unwrap().borrow().val);
            res.extend(rightInorder.into_iter());
            return res;
        }
    }
}

fn main() {
    let mut root = Some(Rc::new(RefCell::new(TreeNode {
        val: 1,
        left: Some(Rc::new(RefCell::new(TreeNode {
            val: 3,
            left: None,
            right: Some(Rc::new(RefCell::new(TreeNode {
                val: 2,
                left: None,
                right: None,
            }))),
        }))),
        right: None,
    })));
    Solution::recover_tree(&mut root);
    println!("{:#?}", root);
}
