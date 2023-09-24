class Solution {
    public int romanToInt(String s) {
        // Create a mapping of Roman numerals to their corresponding values
        Map<Character, Integer> romanToInteger = new HashMap<>();
        romanToInteger.put('I', 1);
        romanToInteger.put('V', 5);
        romanToInteger.put('X', 10);
        romanToInteger.put('L', 50);
        romanToInteger.put('C', 100);
        romanToInteger.put('D', 500);
        romanToInteger.put('M', 1000);

        int result = 0;
        int prevValue = 0;
        
        // Traverse the Roman numeral string from right to left
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            int currValue = romanToInteger.get(c);
            
            // If the current value is less than the previous value, subtract it
            if (currValue < prevValue) {
                result -= currValue;
            } else {
                result += currValue;
            }
            
            // Update the previous value for the next iteration
            prevValue = currValue;
        }
        
        return result; 
    }
}