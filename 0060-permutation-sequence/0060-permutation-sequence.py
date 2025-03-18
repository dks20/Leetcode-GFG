class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        ans = ""
        nums = list(range(1,n+1))
        k-= 1
        #[1,2,3]


        for i in range(n,0,-1):
            iFact = 1     #2
            for q in range(i-1,0,-1):
                iFact *= q
            index = k//iFact
            ans += str(nums[index])
            nums.pop(index)
            k%=iFact
        

        return ans



        
        