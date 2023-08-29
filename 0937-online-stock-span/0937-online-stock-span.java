class StockSpanner {

    private Stack<Integer> prices; // to store the stock prices
    private Stack<Integer> spans;  // to store the stock spans

    public StockSpanner() {
         prices = new Stack<>();
         spans = new Stack<>();
        
    }
    
    public int next(int price) {
        int span = 1; // default span is 1 (the current day itself)
        
        // Check the prices of previous days and pop from stacks until a greater price is encountered
        while (!prices.isEmpty() && prices.peek() <= price) {
            prices.pop();
            span += spans.pop();
        }
        
        // Push the current price and its span onto the stacks
        prices.push(price);
        spans.push(span);
        
        return span;
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */