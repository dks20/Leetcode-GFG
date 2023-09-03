class Solution {
    public String largestNumber(int[] nums) {

        if(nums.length == 0 || nums== null) return"";
        String[] str =  new String[nums.length];
        for(int i=0;i<nums.length;i++){
            str[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(str,(str1,str2) -> (str2+str1).compareTo(str1+str2));
        if(str[0].equals("0")) return "0";

        StringBuilder result = new StringBuilder();
        for(String s : str){
            result.append(s);
        }
        return result.toString();
            
        
    }
}