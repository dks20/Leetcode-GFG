class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        running_sum_freq_map = {0 : 1} # One way to get Running Sum 0, Empty SubArr
        running_sum = 0
        ans = 0

        for i in range(n):
            running_sum += nums[i]

            # For Current Running Sum, Required Sum will be Current_Running_Sum - k
            required_sum = running_sum - k

            # If required_sum is already Appeared
            if required_sum in running_sum_freq_map:
                # We have to update ans with number of times that required_sum Appeared
                ans += running_sum_freq_map[required_sum]

            # Do Append/Update Current_Running_Sum in Map
            if running_sum in running_sum_freq_map:
                # If Already Present, then Do increment its Count/Freq
                running_sum_freq_map[running_sum] += 1
            else:
                 running_sum_freq_map[running_sum] = 1
                    
        return ans
        