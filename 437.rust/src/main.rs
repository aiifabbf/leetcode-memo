/*
.. default-role:: math

统计二叉树里有多少条非空单向（只能从上往下走）路径的节点值累加和是 ``target``

一年前用Python做过这题，用了简单递归。对于二叉树里的每个点，都以这个节点为根节点往下走走试试看能不能走出一条累加和正好是 ``target`` 的路径。复杂度是 `O(n^2)` （吧？），越往下层的节点被重复遍历的次数越多。

今天发现这道题居然又又又能和积分/前缀和扯上关系。可以把这个问题想成这样：先列出从根节点到每个叶子节点的路径，把每条路径都当做array，然后求每条路径里有多少个substring（要连续）的累加和是 ``target`` ，最后加起来。私以为绝妙。

当然不会真的把每条路径都先列出来，那样又是 `O(n^2)` 了。所以我用了回溯，每次先试着往左或者往右走一步，看下有没有以刚才经过的那个节点为最后一个元素的substring累加和正好是target。走完再回退，往另一个方向试试。

梦幻联动其实还是挺难写的。
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

use std::collections::HashMap;

impl Solution {
    // 路径积分/前缀和，O(n)
    #[cfg(feature = "path-integral")]
    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, sum: i32) -> i32 {
        if let Some(root) = &root {
            let mut integrals = vec![0]; // 啥也没遍历的时候，积分值是0
            let mut counter = HashMap::new();
            counter.insert(0, 1);
            let mut res = 0;

            Self::backtrack(&mut integrals, &mut counter, root, sum, &mut res);
            return res as i32;
        } else {
            return 0;
        }
    }

    fn backtrack(
        integrals: &mut Vec<i32>,          // 到choice之前的路径积分
        counter: &mut HashMap<i32, usize>, // 积分值直方图
        choice: &Rc<RefCell<TreeNode>>,    // 这一步将要遍历的节点
        target: i32,                       // substring累加和目标值
        res: &mut usize,                   // 至今发现了多少个substring
    ) {
        let integral = integrals.last().cloned().unwrap_or(0) + choice.borrow().val; // 经过choice节点之后，路径积分值变成了这么多
        if let Some(occurrences) = counter.get(&(integral - target)) {
            // 看下能不能和前面凑几个substring
            *res += occurrences;
        }
        // 统计完之后试着继续往下走，更新积分值array和直方图
        integrals.push(integral);
        *counter.entry(integral).or_insert(0) += 1;

        if let Some(left) = &choice.borrow().left {
            Self::backtrack(integrals, counter, left, target, res); // 试着往左边子树走走
        }
        if let Some(right) = &choice.borrow().right {
            Self::backtrack(integrals, counter, right, target, res); // 试着往右边子树走走
        }

        // 撤销这一步，假装从来没走过choice节点，把积分值array和直方图变回经过choice节点之前的状态
        integrals.pop();
        match counter.get(&integral).cloned() {
            Some(occurrences) => {
                if occurrences == 1 {
                    counter.remove(&integral);
                } else {
                    counter.insert(integral, occurrences - 1);
                }
            }
            _ => {}
        }
    }

    // 简单的递归，O(n^2)
    #[cfg(feature = "recursive")]
    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, sum: i32) -> i32 {
        if let Some(root) = root {
            let mut queue = vec![root];
            let mut res = 0;

            while !queue.is_empty() {
                let mut levelQueue = vec![];

                for node in queue.iter() {
                    if let Some(left) = &node.borrow().left {
                        levelQueue.push(left.clone());
                    }
                    if let Some(right) = &node.borrow().right {
                        levelQueue.push(right.clone());
                    }
                    res += Self::pathSum(node, sum);
                }

                queue = levelQueue;
            }

            return res as i32;
        } else {
            return 0;
        }
    }

    // 这个函数负责计算以root为起点往下有多少条路径积分正好等于target的路径
    fn pathSum(root: &Rc<RefCell<TreeNode>>, target: i32) -> usize {
        let mut res = 0;

        if root.borrow().val == target {
            res += 1;
        }
        if let Some(left) = &root.borrow().left {
            res += Self::pathSum(left, target - root.borrow().val); // 往左边走走，看看能不能凑个target - value
        }
        if let Some(right) = &root.borrow().right {
            res += Self::pathSum(right, target - root.borrow().val); // 往右边也看看，能不能凑个target - value
        }

        return res;
    }

    // 很奇怪啊，加了cache的居然比不加cache还要慢
    fn pathSumCached(
        root: &Rc<RefCell<TreeNode>>,
        target: i32,
        cache: &mut HashMap<(usize, i32), usize>,
    ) -> usize {
        if let Some(res) = cache.get(&(root.as_ptr() as usize, target)) {
            return *res;
        } else {
            let mut res = 0;

            if root.borrow().val == target {
                res += 1;
            }
            if let Some(left) = &root.borrow().left {
                res += Self::pathSumCached(left, target - root.borrow().val, cache);
            }
            if let Some(right) = &root.borrow().right {
                res += Self::pathSumCached(right, target - root.borrow().val, cache);
            }

            cache.insert((root.as_ptr() as usize, target), res);
            return res;
        }
    }
}

fn main() {
    let root = Some(Rc::new(RefCell::new(TreeNode {
        val: 10,
        left: Some(Rc::new(RefCell::new(TreeNode {
            val: 5,
            left: Some(Rc::new(RefCell::new(TreeNode {
                val: 3,
                left: Some(Rc::new(RefCell::new(TreeNode {
                    val: 3,
                    left: None,
                    right: None,
                }))),
                right: Some(Rc::new(RefCell::new(TreeNode {
                    val: -2,
                    left: None,
                    right: None,
                }))),
            }))),
            right: Some(Rc::new(RefCell::new(TreeNode {
                val: 2,
                left: None,
                right: Some(Rc::new(RefCell::new(TreeNode {
                    val: 1,
                    left: None,
                    right: None,
                }))),
            }))),
        }))),
        right: Some(Rc::new(RefCell::new(TreeNode {
            val: -3,
            left: None,
            right: Some(Rc::new(RefCell::new(TreeNode {
                val: 11,
                left: None,
                right: None,
            }))),
        }))),
    })));
    dbg!(Solution::path_sum(root, 8)); // 3

    let root = Some(Rc::new(RefCell::new(TreeNode {
        val: 1,
        left: None,
        right: None,
    })));
    dbg!(Solution::path_sum(root, 0)); // 0
}
