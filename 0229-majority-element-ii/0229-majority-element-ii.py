class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapp = {}
        n = len(nums)
        ans = []

        for i in nums:
            if i in mapp:
                mapp[i] +=1
            else: 
                mapp[i] =1

        for key,values in mapp.items():
            if values > n/3:
                ans.append(key)
        
        return ans