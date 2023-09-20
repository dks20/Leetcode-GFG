class Solution {
    public boolean isHappy(int n) {
      int s = n;
      int f = n;
      
      do{
         s = square(s);
         f = square(square(f));
      }while(s!=f);
         
      if(s ==1){
        return true;
      }
      
      return false;
    }

    private int square(int n){
        int ans = 0;
        while(n >0){
            int rem = n % 10;
            ans += rem * rem;
            n = n/10;
        }
        return ans;
    }

      
    
}