/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <stdlib.h>
struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    if (inorder != 0) {
        TreeNode* root = malloc(sizeof(TreeNode));
        root->val = preorder[0]
        int rootPosition = index(inorder, inorderSize, root->val);

        int* leftTreeInorder = 0;
        leftTreeInorderSize = rootPosition;

        leftTreePreorder = 
    } else {
        return;
    }
}

int index(int* list, int size, int val) {
    for (int i = 0; i < size; i ++) {
        if (val = list[i]) {
            return i;
        }
    }
    return -1;
}