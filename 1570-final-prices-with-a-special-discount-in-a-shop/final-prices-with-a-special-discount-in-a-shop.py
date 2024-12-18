class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        
        for i in range(len(prices)):
            # Start with current price
            current_price = prices[i]
            
            # Look for discount in subsequent items
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    current_price -= prices[j]
                    break
            
            result.append(current_price)
        
        return result