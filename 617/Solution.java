/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        TreeNode node;
        if (t1 != null && t2 != null) {
            node = new TreeNode(t1.val + t2.val);
            node.left = this.mergeTrees(t1.left, t2.left);
            node.right = this.mergeTrees(t1.right, t2.right);
        } else if (t1 != null) {
            node = new TreeNode(t1.val);
            node.left = this.mergeTrees(t1.left, null);
            node.right = this.mergeTrees(t1.right, null);
        } else if (t2 != null) {
            node = new TreeNode(t2.val);
            node.left = this.mergeTrees(null, t2.left);
            node.right = this.mergeTrees(null, t2.right);
        } else {
            node = null;
        }

        return node;
    }
}