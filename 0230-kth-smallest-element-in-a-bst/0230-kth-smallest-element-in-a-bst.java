/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> inorder = new ArrayList<>();
	
    public int kthSmallest(TreeNode root, int k) {
        printInorder(root, k);
        return inorder.get(k-1);
    }
	
    public void printInorder(TreeNode root, int k) {
        if(root != null && inorder.size() < k) {
            printInorder(root.left, k);
            inorder.add(root.val);
            printInorder(root.right, k);
        }
        
    }
}