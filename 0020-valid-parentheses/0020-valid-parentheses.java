class Solution {
    public boolean isValid(String s) {
       Stack<Character> stack = new Stack<>();
        
        // Iterate through each character in the string.
        for (char c : s.toCharArray()) {
            // If the current character is an opening parenthesis, push it onto the stack.
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                // If the current character is a closing parenthesis, check if the stack is empty.
                if (stack.isEmpty()) {
                    return false; // Unmatched closing parenthesis.
                }
                
                // Pop the top element from the stack and check if it matches the current closing parenthesis.
                char top = stack.pop();
                if (c == ')' && top != '(' ||
                    c == ']' && top != '[' ||
                    c == '}' && top != '{') {
                    return false; // Mismatched opening and closing parentheses.
                }
            }
        }
        
        // After processing all characters, the stack should be empty for a valid string.
        return stack.isEmpty(); 
    }
}