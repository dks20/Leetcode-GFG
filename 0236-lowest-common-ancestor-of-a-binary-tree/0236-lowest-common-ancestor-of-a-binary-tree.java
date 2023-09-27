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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null){
            return null;
        }
        if(root == p || root == q){
            return root;
        }

        TreeNode pleft = lowestCommonAncestor(root.left,p,q);
        TreeNode pright = lowestCommonAncestor(root.right,p,q);

        if(pleft != null && pright != null){
            return root;
        }

        return pleft == null ? pright : pleft ;


        
    }
}