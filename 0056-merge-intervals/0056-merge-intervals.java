class Solution {
    public int[][] merge(int[][] intervals) {

        Arrays.sort(intervals , (a,b) -> Integer.compare(a[0],b[0]));
        Stack<int[]> stack = new Stack();
        stack.add(intervals[0]);

        for(int i =1; i< intervals.length ; i++){
            int startPoint2 = intervals[i][0];
            int endPoint2 = intervals[i][1];

            int[] arraystack = stack.pop();

            int startPoint1 = arraystack[0];
            int endPoint1 = arraystack[1];

            int endMax = Math.max(endPoint1,endPoint2);

            if(startPoint2 <= endPoint1){
                int[] merge = new int[]{startPoint1 , endMax};
                stack.add(merge);

            }else{
                stack.add(arraystack);
                stack.add(intervals[i]);
            }


        }
        int[][] result = new int[stack.size()][2];
        for(int i = result.length -1 ; i>= 0 ; i-- ){
            int[] stackpop = stack.pop();
            result[i][0] = stackpop[0] ;
            result[i][1] = stackpop[1] ;
        }
        return result;
        
    }
}