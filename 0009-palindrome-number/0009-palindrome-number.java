class Solution {
    public boolean isPalindrome(int x) {
         // Convert the integer to a string
        String str = Integer.toString(x);
        
        // Use two pointers to compare characters from the start and end
        int left = 0;
        int right = str.length() - 1;
        
        while (left < right) {
            // Compare characters at the left and right pointers
            if (str.charAt(left) != str.charAt(right)) {
                return false; // If they don't match, it's not a palindrome
            }
         // Move the pointers towards each other
            left++;
            right--;
        }
        
        return true; // If the loop completes, it's a palindrome
        
    }
}