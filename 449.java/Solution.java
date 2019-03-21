import java.util.Queue;

public class Codec {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        Queue<TreeNode> queue = new sun.misc.Queue();
        queue.add(root);
        StringBuilder res = new StringBuilder();

        while(!queue.isEmpty()) {
            TreeNode i = queue.poll();
            if(i.left != null) {
                queue.add(i.left);
            }
            if(i.right != null) {
                queue.add(i.right);
            }
            res.append(i.left);
            res.append(i.right);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {

    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));