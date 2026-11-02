class Solution(object):
    def maxProfit(self, prices):
        left = 0
        best = 0
        for right, price in enumerate(prices):
            if price < prices[left]:
                left = right
            elif price > prices[left]:
                profit = price - prices[left]
                if profit > best:
                    best = profit
        return best

        # Note: this is basically a two pointer question
        # Time complexity = O(n)
        # Space complexity = O(1)

        