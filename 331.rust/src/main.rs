/*
给一个先根遍历路径，类似 ``2,#,3,4,#`` 这种， ``#`` 表示空节点（也就是null）。问是否是一个合法的二叉树先根遍历路径。

一看到这个题目就想到以前做过的一道 `验证是否是二分搜索树的先根遍历 <https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/>`_ 的题目。这题也用插槽的思想，非常方便。

首先要把实节点和空节点都当做是普通的节点，但是这两种节点对插槽的影响是不同的

-   一个实节点会占据一个插槽，但是插入进去之后，会在下方创建出两个新的插槽
-   一个空节点只会占据一个插槽，插入进去之后，不会创建新的插槽

然后我们试着从先根遍历路径重建这个二叉树。

一开始什么节点都没插入之前，树是空的，所以只有一个插槽，这个插槽是用来填根节点的。那么第一个节点是啥呢？有两种可能

-   第一个节点就是空节点 ``#``

    那么null插入进去之后，下面就不能再放节点了。如果下面还有东西，说明出错。

-   第一个节点是实节点

    那么它会占据一个插槽，并且创建两个新的插槽。

如果在重建过程中发现，下面还有节点要插入，可是没有插槽了，这说明这是个非法的先根遍历路径。

同样，如果重建完了之后，发现居然还有插槽没有用掉，也说明这是个非法的先根遍历路径。

.. 惊讶地发现早就 `有人 <https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78564/The-simplest-python-solution-with-explanation-(no-stack-no-recursion)>`_ 也提出插槽的思想了。
*/

struct Solution;

impl Solution {
    pub fn is_valid_serialization(preorder: String) -> bool {
        let mut stack = vec![0]; // 0表示可用的插槽，其实放什么无所谓。一开始树是空的，只能放根节点，所以只有一个插槽

        for v in preorder.split(",") {
            match v {
                "#" => {
                    // 空节点
                    if stack.is_empty() {
                        // 没有插槽可用了
                        return false;
                    } else {
                        // 这个插槽放空节点
                        stack.pop(); // 空节点占用插槽，不创建新插槽
                    }
                }
                _ => {
                    // 实节点
                    if stack.is_empty() {
                        // 没有插槽可用了
                        return false;
                    } else {
                        stack.push(0); // 实节点占用一个插槽、创建两个新插槽。等效于创建一个新插槽
                    }
                }
            }
        }

        return stack.is_empty(); // 重建完了。如果插槽正好全部用完，说明可以。如果没用完，说明是非法的先根遍历路径
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::is_valid_serialization("9,3,4,#,#,1,#,#,2,#,6,#,#".to_string())
    ); // true
    println!("{:?}", Solution::is_valid_serialization("1,#".to_string())); // false
    println!(
        "{:?}",
        Solution::is_valid_serialization("9,#,#,1".to_string())
    ); // false
    println!(
        "{:?}",
        Solution::is_valid_serialization("9,#,92,#,#".to_string())
    ); // true
}
