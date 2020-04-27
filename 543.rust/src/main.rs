/*
二叉树中两个节点中间最多能隔多少条边

.. Python版有更详细的解释。不过是一年前写的了。

也就是求二叉树里面任意挑选两个节点、这两个节点距离的最大值。这个路径不一定要经过根节点的，因为经过根节点的也不一定是最长的路径。

如果把二叉树想成图就没必要了。思考一下，两个节点距离的最大值，能不能退化成某个可以递归的问题？可以的。二叉树里面的路径，要么往上走，要么往下走。不如统一成只能往下走，把问题退化成，对于二叉树里面每一个节点，我都作为根节点，看从这个节点分别往左边能走多深、往右边能走多深，这两个深度加起来，就是经过这个节点的最长路径了。

同样的配方、同样的口味，用Rust又写了一遍。

用Rust有一个坑的地方，就是缓存怎么办。TreeNode是不能自动derive Hash trait的，因为Option<Rc<RefCell<TreeNode>>>没实现Hash。所以只能把RefCell<TreeNode>的地址作为缓存的key。Rc有一个 ``.into_raw()`` 方法，可以得到指向对象的裸指针。

只要不解引用裸指针都是安全的，所以完全没问题。
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

use std::cmp::max;
use std::collections::HashMap;
use std::collections::VecDeque;

impl Solution {
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }

        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());
        let mut cache = HashMap::new();
        let mut res = 0;

        while !queue.is_empty() {
            let node = queue.pop_front().unwrap();
            let mut longestPathThroughHere = 1;

            for child in vec![node.borrow().left.as_ref(), node.borrow().right.as_ref()].into_iter()
            {
                // 下面这一坨要我写两遍我实在是不愿意的……
                if let Some(inner) = child {
                    longestPathThroughHere +=
                        Solution::longestPathFromCached(&Some(inner.clone()), &mut cache);
                    queue.push_back(inner.clone());
                }
            }

            res = max(res, longestPathThroughHere);
        }

        return res - 1;
    }

    fn longestPathFromCached(
        root: &Option<Rc<RefCell<TreeNode>>>,
        cache: &mut HashMap<*const RefCell<TreeNode>, i32>, // cache的key是裸指针
    ) -> i32 {
        // println!("{:?}", cache);
        return match root {
            Some(inner) => {
                let key = Rc::into_raw(inner.clone());
                match cache.get(&key) {
                    Some(v) => v.clone(),
                    None => {
                        let value = 1 + max(
                            Solution::longestPathFromCached(&inner.borrow().left, cache),
                            Solution::longestPathFromCached(&inner.borrow().right, cache),
                        );
                        cache.insert(key, value);
                        value
                    }
                }
            }
            None => 0,
        };
    }
}

fn main() {
    println!(
        "{:#?}",
        Solution::diameter_of_binary_tree(Some(Rc::new(RefCell::new(TreeNode {
            val: 1,
            left: Some(Rc::new(RefCell::new(TreeNode {
                val: 2,
                left: Some(Rc::new(RefCell::new(TreeNode {
                    val: 4,
                    left: None,
                    right: None,
                }))),
                right: Some(Rc::new(RefCell::new(TreeNode {
                    val: 5,
                    left: None,
                    right: None,
                })))
            }))),
            right: Some(Rc::new(RefCell::new(TreeNode {
                val: 3,
                left: None,
                right: None,
            }))),
        }))))
    ); // 3
}
