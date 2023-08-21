class Solution {
    public boolean isIdealPermutation(int[] nums) {
        int n = nums.length;
        int maxSeen = -1; // Initialize maxSeen as -1
        
        for (int i = 0; i < n - 2; i++) {
            maxSeen = Math.max(maxSeen, nums[i]); // Update maxSeen
            
            // If the current element is greater than the element two positions ahead,
            // return false as it's a non-local inversion
            if (maxSeen > nums[i + 2]) {
                return false;
            }
        }
        
        return true;
        
    }
}