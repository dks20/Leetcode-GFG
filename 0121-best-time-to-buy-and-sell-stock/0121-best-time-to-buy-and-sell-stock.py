class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
                sell =  buy+1
            else:
                profit = prices[sell] - prices[buy]
                maxProf = max(maxProf,profit)
                sell += 1
            
            

        return maxProf
       
            
        

        