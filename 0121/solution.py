from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]  # Track the minimum price seen so far
        max_profit = 0
        
        for price in prices:
            # Update minimum price if we find a lower price
            min_price = min(min_price, price)
            # Calculate potential profit if we sell at current price
            current_profit = price - min_price
            # Update maximum profit if current profit is higher
            max_profit = max(max_profit, current_profit)
        
        return max_profit