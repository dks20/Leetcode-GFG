class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0; // If the array is empty, there are no duplicates to remove.
        }

        int uniqueIndex = 0; // Index to keep track of the unique elements.

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[uniqueIndex]) {
                // If the current element is different from the unique element, move to the next unique element.
                uniqueIndex++;
                nums[uniqueIndex] = nums[i];
            }
            // If the current element is the same as the unique element, it's a duplicate; skip it.
        }

        // The length of the modified array is (uniqueIndex + 1).
        return uniqueIndex + 1;
    }
}