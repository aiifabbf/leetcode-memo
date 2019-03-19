import java.util.Stack;

import javax.swing.tree.TreeNode;

import sun.misc.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        Queue<Integer> queue = new Queue<>();
        Stack stack = new Stack();
        stack.peek();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {

    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));