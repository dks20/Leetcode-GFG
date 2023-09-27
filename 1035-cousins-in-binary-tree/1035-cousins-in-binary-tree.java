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
    public boolean isCousins(TreeNode root, int x, int y) {
        if(root == null){
            return false;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()){
            int size= queue.size();
            boolean isExixtX = false;
            boolean isExixtY = false;
            
            for(int i = 0; i< size ; i++){
                TreeNode curr = queue.poll();
                if(curr.val == x){
                     isExixtX = true;
                }
                if(curr.val == y){
                     isExixtY = true;
                }
                if(curr.left != null && curr.right != null){
                   if(curr.left.val == x && curr.right.val == y){
                     return false;
                   }
                   if(curr.left.val == y && curr.right.val == x){
                     return false;
                   }
                   
                   
                  
                }
                if(curr.left != null){
                    queue.offer(curr.left);

                }
                if(curr.right != null){
                    queue.offer(curr.right);
                    
                }

            }
            if (isExixtX && isExixtY){
                return true;
            }
        }
        return false;
        
    }
}