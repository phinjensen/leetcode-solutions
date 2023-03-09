# Top-down, O(n) solution.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.memo = {}
        self.prices = prices
        return self.helper(0, True)
    
    def helper(self, start: int, can_buy: bool) -> int:
        if (start, can_buy) in self.memo:
            return self.memo[(start, can_buy)]
        if start >= len(self.prices):
            return 0
        if can_buy:
            result = max(
                -self.prices[start] + self.helper(start + 1, False), # buy
                self.helper(start + 1, True) # nothing
            )
        else:
            result = max(
                self.prices[start] + self.helper(start + 2, True), # sell
                self.helper(start + 1, False) # nothing
            )
        self.memo[(start, can_buy)] = result
        return result
