# Submitted solution (failed)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = len(prices) - 1
        out = 0

        while p2 > p1:
            if (prices[p2] - prices[p1] > out):
                out = prices[p2] - prices[p1]
                p2 -= 1
            else:
                p1 += 1
            
        return out 
        

# Optimized solution
# https://www.youtube.com/watch?v=1pkOgXD63yU
# I guess this is a sliding window as well

class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p1 = 0 # Buy
        p2 = 1 # Sell
        profit = 0

        while p2 < len(prices):
            if prices[p2] > prices[p1]:
                profit = max(prices[p2] - prices[p1], profit)
            else:
                # Swap occurs as we have a better buying price
                p1 = p2
            p2 += 1
        return profit
    
# TODO: Kadane's algorithm (Dynamic Programming)