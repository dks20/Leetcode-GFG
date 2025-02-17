class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        n = len(nums)//3
        ans = []
        
        for i in nums:
            
            count[i] += 1
            
        for key,values in count.items():
            if values > n:
                ans.append(key)
        

        return ans 



