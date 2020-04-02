/* 
从inorder和postorder遍历恢复出原来的二叉树。

大致原理是，观察inorder和postorder遍历得到的array的结构。inorder是这样的

::

    [   ] o (   )

``[]`` 表示左子树、 ``o`` 表示根节点、 ``()`` 表示右子树。

postorder是这样的

::

    [   ] (   ) o

所以直接取postorder的最后一个元素 ``o`` ，这个元素肯定是根节点的值。

然后需要确定左子树的边界，怎么确定呢？很简单，到inorder里面去定位 ``o`` 的位置不就好了？ ``o`` 之前的肯定是左子树的inorder， ``o`` 之后的肯定是右子树的inorder。

假设 `i` 就是 ``o`` 在inorder里面的下标，那么一切都真相大白了

-   ``inorder[: i]`` 是左子树的inorder遍历结果
-   ``inorder[i + 1: ]`` 是右子树的inorder遍历结果
-   ``postorder[: i]`` 是左子树的postorder遍历结果
-   ``postorder[i: -1]`` 是右子树的postorder遍历结果

这四样东西分成两组塞到下一层函数了，就好了。

老题了，这次用rust重新写一遍。更详细的解释在python版里。
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
    pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        return Solution::treeFromInorderPostorder(&inorder[..], &postorder[..]);
    }

    fn treeFromInorderPostorder(
        inorder: &[i32],
        postorder: &[i32],
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if inorder.is_empty() {
            return None;
        }

        let rootValue = postorder.last().unwrap().clone(); // postorder的最后一个元素肯定是根节点的值
        let mut root = Some(Rc::new(RefCell::new(TreeNode::new(rootValue)))); // 建立根节点
        let mut boundary = 0; // inorder里左子树的右边界

        for i in 0..inorder.len() {
            // 到inorder里面去找根节点值的位置
            if rootValue == inorder[i] {
                // 找到了
                boundary = i;
                break;
            }
        } // 如果没找到，说明左子树是空的，那么正好boundary是0，也就不用管了

        let leftInorder = &inorder[..boundary]; // 左子树的inorder遍历结果
        let leftPostorder = &postorder[..boundary]; // 左子树的postorder遍历结果

        let rightInorder = &inorder[boundary + 1..]; // 右子树的inorder遍历结果
        let rightPostorder = &postorder[boundary..postorder.len() - 1]; // 右子树的postorder遍历结果

        root.as_mut().unwrap().borrow_mut().left =
            Solution::treeFromInorderPostorder(leftInorder, leftPostorder); // 递归地重建左子树
        root.as_mut().unwrap().borrow_mut().right =
            Solution::treeFromInorderPostorder(rightInorder, rightPostorder); // 递归地重建右子树

        return root;
    }
}

fn main() {
    println!(
        "{:#?}",
        Solution::build_tree(vec![9, 3, 15, 20, 7], vec![9, 15, 7, 20, 3])
    ); // {:#?}可以变漂亮
}
