class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        f = nums[0]
        s = nums[0]

        fc , sc =0,0

        for num in nums:
            if num == f:
                fc +=1
            elif num == s:
                sc += 1
            elif fc == 0:
                f = num
                fc +=1
            elif sc == 0:
                s = num
                sc +=1
            else:
                fc -= 1
                sc -= 1

        fc = sc = 0
        for num in nums:
            if num == f:
                fc += 1
            elif num == s:
                sc += 1

        # Step 3: Return candidates with count > n // 3
        result = []
        n = len(nums)
        if fc > n // 3:
            result.append(f)
        if sc > n // 3:
            result.append(s)
        return result


