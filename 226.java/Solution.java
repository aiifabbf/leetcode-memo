// 这个好简单啊……不知道为什么homebrew作者这个都不会写……直接调换left和right，再递归地，以left为根节点调换子树，以right为根节点调换子树。

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root != null) { // root有可能为null的吧……
            TreeNode tempTreeNode = root.left;
            root.left = root.right;
            root.right = tempTreeNode; // 完成了这一层的调换
            this.invertTree(root.left); // left子树调换
            this.invertTree(root.right); // right子树调换
        }
        return root;
    }
}