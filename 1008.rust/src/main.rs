/*
.. default-role:: math

从先根遍历路径还原出二分搜索树

挺简单的，想想二分搜索树的特点，左边子树里面的所有节点都小于根节点，右边子树里面的所有节点都大于根节点。先根遍历大概长这样

::

    o [    ] (    )

所以第一个元素一定是根节点。然后往右边一个一个看过去，看到的第一个比根节点还大的节点，一定是右边子树的起始位置。再递归地建立左边子树和右边子树就可以了。

这样是最直观的，但是复杂度其实挺高的，应该是 `O(n^2)` 吧。为什么会这么慢呢？因为找到右边子树的起始位置之后，把左边子树传到下一层函数处理时，又要扫描一遍左边子树，找到第一个比左边子树的根节点大的节点。

所以不用多说了，既然要扫，不如扫一遍就把array里面每个元素后面第一个比这个元素大的元素位置找出来，以后就不用再扫描了，直接查表就能找到任意一个元素后面第一个比当前元素的大元素下标。

这件事情怎么做？也是套路，用单调递减stack做。

那怎么把这个辅助缓存传下去呢？如果算出来的是绝对坐标，那么传到下一层不就不对了吗。也很容易解决，不要算绝对坐标就好了，算出相对坐标。假设第 `i` 个元素后面第一个比第 `i` 个元素大的元素下标是 `j` ，那么不要记 ``cache[i] = j`` ，记 ``cache[i] = j - i`` 。
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

use std::collections::VecDeque;

impl Solution {
    // O(n)加速做法
    #[cfg(feature = "cached")]
    pub fn bst_from_preorder(preorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut firstGreaterIndexDelta = vec![Option::<usize>::None; preorder.len()]; // firstGreaterIndexDelta[i]表示后面第一个比第i个元素大的元素的下标是i + firstGreaterIndexDelta[i]
        let mut stack: Vec<(usize, i32)> = vec![];

        for (i, v) in preorder.iter().enumerate() {

            while !stack.is_empty() {
                // 不停地pop，直到stack的最后一个元素比将要push进来的元素大为止。也就是维持stack的单调递减特性
                if stack.last().unwrap().1 < *v {
                    // stack的最后一个元素小于要插入的元素
                    let (j, w) = stack.pop().unwrap(); // 那么第j个元素后面第一个比它大的元素下标就找到了
                    firstGreaterIndexDelta[j] = Some(i - j); // 不要记绝对坐标，记相对坐标
                } else {
                    break;
                }
            }

            stack.push((i, *v));
        }

        return Solution::bstFromPreorderCached(&preorder[..], &firstGreaterIndexDelta[..]);
    }

    // O(n^2)普通做法
    #[cfg(feature = "naive")]
    pub fn bst_from_preorder(preorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        return Solution::bstFromPreorder(&preorder[..]);
    }

    fn bstFromPreorderCached(
        preorder: &[i32],
        firstGreaterIndexDelta: &[Option<usize>],
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if preorder.is_empty() {
            return None;
        } else {
            let rootValue = preorder[0];
            let rightTreeStartIndex = match firstGreaterIndexDelta[0] {
                Some(i) => i,
                None => preorder.len(),
            }; // 直接O(1)查出后面比根节点大的第一个元素的下标

            let mut inner = Rc::new(RefCell::new(TreeNode::new(rootValue)));
            inner.borrow_mut().left = Solution::bstFromPreorderCached(
                &preorder[1..rightTreeStartIndex],
                &firstGreaterIndexDelta[1..rightTreeStartIndex],
            ); // preorder和cache切同样的部分
            inner.borrow_mut().right = Solution::bstFromPreorderCached(
                &preorder[rightTreeStartIndex..],
                &firstGreaterIndexDelta[rightTreeStartIndex..],
            ); // 这里也是切同样的部分
            return Some(inner);
        }
    }

    fn bstFromPreorder(preorder: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
        if preorder.is_empty() {
            return None;
        } else {
            let rootValue = preorder[0];
            let mut rightTreeStartIndex = preorder.len();

            for (i, v) in preorder.iter().enumerate().skip(1) {
                if v > &rootValue {
                    rightTreeStartIndex = i;
                    break;
                }
            }

            let mut inner = Rc::new(RefCell::new(TreeNode::new(rootValue)));
            inner.borrow_mut().left = Solution::bstFromPreorder(&preorder[1..rightTreeStartIndex]);
            inner.borrow_mut().right = Solution::bstFromPreorder(&preorder[rightTreeStartIndex..]);
            return Some(inner);
        }
    }
}

fn main() {
    println!(
        "{:#?}",
        Solution::bst_from_preorder(vec![8, 5, 1, 7, 10, 12])
    );
}
